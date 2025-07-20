import requests
import threading
import time
import random

# 🔧 Server details
URL = "http://localhost:8000/invoke"

# 🧠 Functions to test
functions_to_test = [
    {"function": "hello", "params": {"name": "Shivani"}},
    {"function": "cpu_burn", "params": {"iterations": 5000000}},
    {"function": "memory_alloc", "params": {"size": 10000000}},
    {"function": "sort", "params": {"data": [random.randint(0, 10000) for _ in range(10000)]}}
]

CONCURRENT_CALLS = 15  # 🔁 Total concurrent requests

def invoke_function(thread_id):
    func = random.choice(functions_to_test)  # Pick a function randomly
    try:
        start = time.time()
        response = requests.post(URL, json=func)
        elapsed = time.time() - start
        print(f"[Thread {thread_id}] {func['function']} | {elapsed:.3f}s | {response.json()}")
    except Exception as e:
        print(f"[Thread {thread_id}] Error: {e}")

# 🚀 Launch threads
threads = []
for i in range(CONCURRENT_CALLS):
    t = threading.Thread(target=invoke_function, args=(i,))
    t.start()
    threads.append(t)

# ✅ Wait for all to finish
for t in threads:
    t.join()

print("All multi-function concurrent invocations completed.")
