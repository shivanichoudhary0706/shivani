import json
import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the log file
log_path = "handler/execution_log.jsonl"

if not os.path.exists(log_path):
    print(f"Log file not found at {log_path}")
    exit(1)

# Load execution log
with open(log_path, 'r') as f:
    records = [json.loads(line) for line in f]

# Create DataFrame
df = pd.DataFrame(records)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot execution time for each function
plt.figure(figsize=(10, 6))
for func in df['function'].unique():
    subset = df[df['function'] == func]
    plt.plot(subset['timestamp'], subset['execution_time'], marker='o', label=func)

plt.title('Function Execution Time Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Execution Time (seconds)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
