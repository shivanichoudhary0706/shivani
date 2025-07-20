# concurrent_multi_test.py
import httpx
import asyncio
import time
import random
import json

# 🔧 Server details
BASE_URL = "http://localhost:8000"
INVOKE_URL = f"{BASE_URL}/invoke"
API_KEY = "your_super_secret_api_key" # Match this with the API_KEY in server.py

# 🧠 Functions to test
functions_to_test = [
    {"function": "hello", "params": {"name": "Shivani"}},
    {"function": "cpu_burn", "params": {"iterations": 500000}},
    {"function": "memory_alloc", "params": {"size": 1000000}},
    {"function": "sort", "params": {"data": [random.randint(0, 10000) for _ in range(1000)]}}
]

CONCURRENT_CALLS = 15  # 🔁 Total concurrent requests
REQUEST_TIMEOUT = 10 # seconds
MAX_RETRIES = 3
RETRY_DELAY = 0.5 # seconds
ENABLE_COLD_START_TEST = True # Set to True to periodically force cold starts for analysis

async def invoke_function_async(task_id: int):
    func_payload = random.choice(functions_to_test).copy() # Use .copy() to avoid modifying original dict
    function_name = func_payload['function']
    retries = 0

    # Periodically force a cold start for specific tasks for better observation
    if ENABLE_COLD_START_TEST and task_id % 5 == 0: # Every 5th task, for example
        func_payload['simulate_cold_start'] = True

    while retries < MAX_RETRIES:
        try:
            start = time.time()
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                headers = {"X-API-Key": API_KEY}
                response = await client.post(INVOKE_URL, json=func_payload, headers=headers)
                response.raise_for_status() # Raise an exception for 4xx/5xx responses
            elapsed = time.time() - start
            response_json = response.json()
            req_id = response_json.get('request_id', 'N/A')
            status_message = response_json.get('message', 'No message')
            exec_time = response_json.get('execution_time', 'N/A')

            print(f"[Task {task_id}] {function_name} | Req ID: {req_id} | Total Time: {elapsed:.3f}s | Exec Time: {exec_time:.3f}s | Status: {status_message}")
            break # Exit retry loop on success
        except httpx.TimeoutException:
            retries += 1
            print(f"[Task {task_id}] {function_name} | Timeout after {REQUEST_TIMEOUT}s. Retrying ({retries}/{MAX_RETRIES})...")
            await asyncio.sleep(RETRY_DELAY)
        except httpx.HTTPStatusError as e:
            retries += 1
            error_detail = e.response.json().get("detail", "No detail provided")
            print(f"[Task {task_id}] {function_name} | HTTP Error {e.response.status_code}: {error_detail}. Retrying ({retries}/{MAX_RETRIES})...")
            await asyncio.sleep(RETRY_DELAY)
        except httpx.RequestError as e:
            retries += 1
            print(f"[Task {task_id}] {function_name} | Request Error: {e}. Retrying ({retries}/{MAX_RETRIES})...")
            await asyncio.sleep(RETRY_DELAY)
        except json.JSONDecodeError:
            retries += 1
            print(f"[Task {task_id}] {function_name} | Failed to decode JSON response. Retrying ({retries}/{MAX_RETRIES})...")
            await asyncio.sleep(RETRY_DELAY)
        except Exception as e:
            print(f"[Task {task_id}] {function_name} | Unexpected Error: {e}")
            break # Do not retry for unexpected errors

    if retries == MAX_RETRIES:
        print(f"[Task {task_id}] {function_name} | Failed after {MAX_RETRIES} retries.")


async def main():
    print(f"Starting {CONCURRENT_CALLS} concurrent invocations...")
    tasks = [invoke_function_async(i) for i in range(CONCURRENT_CALLS)]
    await asyncio.gather(*tasks)
    print("All multi-function concurrent invocations completed.")

if __name__ == "__main__":
    asyncio.run(main())