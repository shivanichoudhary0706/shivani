import importlib.util
import sys
import json
import time
from datetime import datetime
import os

def load_and_run(file_path, event):
    # Load user module from file
    spec = importlib.util.spec_from_file_location("user_module", file_path)
    user_module = importlib.util.module_from_spec(spec)
    sys.modules["user_module"] = user_module
    spec.loader.exec_module(user_module)

    #  Start timing
    start_time = time.time()

    #  Call user function
    result = user_module.handler(event)

    #  End timing
    end_time = time.time()
    execution_time = end_time - start_time

    #  Prepare API output
    output = {
        "result": result,
        "execution_time": execution_time
    }

    #  Output to API (stdout)
    print(json.dumps(output))

    #  Append to execution log file
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "function": os.path.basename(file_path),
        "params": event,
        "execution_time": execution_time
    }

    try:
        with open("/handler/execution_log.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        print("Log written", file=sys.stderr)  # Debug confirmation
    except Exception as e:
        print(f"Failed to write log: {e}", file=sys.stderr)

if __name__ == "__main__":
    file_path = os.environ.get("FUNC_FILE", "/functions/hello.py")
    input_event = os.environ.get("FUNC_EVENT", "{}")

    event = json.loads(input_event)
    load_and_run(file_path, event)
