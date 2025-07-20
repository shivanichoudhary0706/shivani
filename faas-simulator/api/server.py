# api/server.py
from fastapi import FastAPI, HTTPException, Request, Depends, status
from pydantic import BaseModel, Field, ValidationError
import importlib.util
import sys
import time
import os
import json
import uuid
import asyncio
import pandas as pd # Used for pd.Timestamp.now() for consistent logging format
from typing import Union

# --- Configuration ---
API_KEY = os.getenv("API_KEY", "your_super_secret_api_key")
FUNCTIONS_DIR = "/functions"
LOG_FILE = "/handler/execution_log.jsonl" # Path for logging execution

# --- Cold Start Simulation ---
# This dictionary will keep track of when each function was last invoked.
# If a function hasn't been invoked for COLD_START_THRESHOLD_SECONDS,
# the next invocation will be considered a cold start.
COLD_START_THRESHOLD_SECONDS = 5 # Functions inactive for 5 seconds will cold start
COLD_START_DELAY_SECONDS = 0.5   # Delay added for cold starts (simulating initialization)
cold_start_tracker = {} # {function_name: last_invoked_timestamp}

app = FastAPI(
    title="Enhanced Function Invocation API",
    description="API to dynamically invoke Python functions with improved robustness and concurrency.",
    version="1.0.0"
)

# --- Models ---
class FunctionParams(BaseModel):
    pass

class InvokeRequest(BaseModel):
    function: str = Field(..., description="Name of the function to invoke")
    params: dict = Field({}, description="Dictionary of parameters to pass to the function")
    simulate_cold_start: bool = Field(False, description="Force a cold start for this invocation (for testing)")

class InvokeResponse(BaseModel):
    request_id: str
    function: str
    result: Union[dict, None] = None # <--- CHANGE THIS LINE
    execution_time: Union[float, None] = None # <--- CHANGE THIS LINE
    message: str


# --- API Key Authentication Dependency ---
def verify_api_key(request: Request):
    api_key_header = request.headers.get("X-API-Key")
    if not api_key_header or api_key_header != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    return api_key_header

# --- Function Loading ---
def load_function(function_name: str):
    module_path = os.path.join(FUNCTIONS_DIR, f"{function_name}.py")
    if not os.path.exists(module_path):
        return None

    try:
        # Check if module is already loaded (avoids re-loading if not strictly necessary)
        if function_name in sys.modules:
            module = sys.modules[function_name]
            return getattr(module, function_name, None)

        spec = importlib.util.spec_from_file_location(function_name, module_path)
        if spec is None:
            return None
        module = importlib.util.module_from_spec(spec)
        sys.modules[function_name] = module
        spec.loader.exec_module(module)
        return getattr(module, function_name, None)
    except Exception as e:
        print(f"Error loading function {function_name}: {e}")
        return None

# --- Logging Helper ---
def log_execution(record: dict):
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(json.dumps(record) + '\n')
    except IOError as e:
        print(f"Error writing to log file {LOG_FILE}: {e}")
    except Exception as e:
        print(f"Unexpected error during logging: {e}")


# --- API Endpoint ---
@app.post("/invoke", response_model=InvokeResponse, status_code=status.HTTP_200_OK)
async def invoke_function_endpoint(
    request_body: InvokeRequest,
    api_key: str = Depends(verify_api_key) # Secure with API Key
):
    function_name = request_body.function
    params = request_body.params
    simulate_cold_start = request_body.simulate_cold_start
    request_id = str(uuid.uuid4())
    is_cold_start = False

    # --- Cold Start Logic ---
    current_time = time.time()
    if simulate_cold_start or \
       function_name not in cold_start_tracker or \
       (current_time - cold_start_tracker.get(function_name, 0) > COLD_START_THRESHOLD_SECONDS):
        is_cold_start = True
        # Simulate cold start delay
        await asyncio.sleep(COLD_START_DELAY_SECONDS)
        print(f"Simulating cold start for '{function_name}' (Request ID: {request_id})")
    cold_start_tracker[function_name] = current_time # Update last invoked time

    func = load_function(function_name)
    if func is None:
        error_message = f"Function '{function_name}' not found or could not be loaded."
        log_record = {
            "request_id": request_id,
            "timestamp": pd.Timestamp.now().isoformat(),
            "function": function_name,
            "execution_time": 0.0,
            "status": "failure",
            "error": error_message,
            "is_cold_start": is_cold_start
        }
        log_execution(log_record)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_message
        )

    start_time = time.time()
    result = None
    error_message = None

    try:
        # In a real async invocation, you'd put this into a task queue.
        # For this demo, we execute directly but return task_id conceptually.
        result = func(**params)
        end_time = time.time()
        execution_time = end_time - start_time
        status_msg = "success"
        response_message = "Function executed successfully."

    except ValidationError as e:
        error_message = f"Parameter validation error: {e.errors()}"
        status_msg = "failure"
        execution_time = time.time() - start_time
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=error_message
        )
    except TypeError as e:
        error_message = f"Function '{function_name}' received incorrect parameters: {e}"
        status_msg = "failure"
        execution_time = time.time() - start_time
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_message
        )
    except Exception as e:
        error_message = f"An unexpected error occurred during function execution: {e}"
        status_msg = "failure"
        execution_time = time.time() - start_time
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error_message
        )
    finally:
        # Log the execution regardless of success or failure
        log_record = {
            "request_id": request_id,
            "timestamp": pd.Timestamp.now().isoformat(),
            "function": function_name,
            "execution_time": execution_time,
            "status": status_msg,
            "error": error_message,
            "is_cold_start": is_cold_start
        }
        log_execution(log_record)


    return InvokeResponse(
        request_id=request_id,
        function=function_name,
        result={"output": result},
        execution_time=execution_time,
        message=response_message
    )

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Enhanced Function Invocation API"}