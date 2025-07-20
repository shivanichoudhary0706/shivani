import json
import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.dates as mdates
import numpy as np

# Path to the log file
log_path = "handler/execution_log.jsonl"

if not os.path.exists(log_path):
    print(f"Log file not found at {log_path}")
    print("Please ensure you have run 'docker-compose up -d' and 'python concurrent_multi_test.py' first to generate logs.")
    exit(1)

# Load execution log
records = []
try:
    with open(log_path, 'r') as f:
        for line in f:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Skipping malformed JSON line: {line.strip()} - Error: {e}")
except IOError as e:
    print(f"Error reading log file {log_path}: {e}")
    exit(1)

if not records:
    print("No valid records found in the log file. Make sure your API is logging correctly.")
    exit(0)

# Create DataFrame
df = pd.DataFrame(records)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Ensure execution_time is numeric and handle potential missing values
df['execution_time'] = pd.to_numeric(df['execution_time'], errors='coerce')

# Filter for successful invocations for performance analysis
successful_df = df[df['status'] == 'success'].copy()

print("\n--- Overall Statistics ---")
total_invocations = len(df)
successful_invocations_count = len(successful_df)
failed_invocations_count = total_invocations - successful_invocations_count

print(f"Total Invocations: {total_invocations}")
print(f"Successful Invocations: {successful_invocations_count}")
print(f"Failed Invocations: {failed_invocations_count}")
if total_invocations > 0:
    print(f"Success Rate: {successful_invocations_count/total_invocations:.2%}")
    print(f"Error Rate: {failed_invocations_count/total_invocations:.2%}")

print("\n--- Performance Metrics by Function ---")
unique_functions = successful_df['function'].unique()
for func_name in unique_functions:
    func_df = successful_df[successful_df['function'] == func_name]

    if not func_df.empty:
        cold_starts = func_df[func_df['is_cold_start'] == True]
        warm_starts = func_df[func_df['is_cold_start'] == False]

        print(f"\nFunction: '{func_name}'")
        print(f"  Total Successful Invocations: {len(func_df)}")

        if 'is_cold_start' in func_df.columns and not func_df['is_cold_start'].dropna().empty:
            print(f"  Cold Starts: {len(cold_starts)} ({len(cold_starts)/len(func_df):.2%} of successful)")
            print(f"  Warm Starts: {len(warm_starts)} ({len(warm_starts)/len(func_df):.2%} of successful)")
        else:
            print("  Cold/Warm start data not available or empty for this function.")

        print("  --- All Successful Invocations ---")
        if not func_df['execution_time'].empty:
            print(f"    Mean Execution Time: {func_df['execution_time'].mean():.4f}s")
            print(f"    Median Execution Time (P50): {func_df['execution_time'].median():.4f}s")
            print(f"    90th Percentile (P90): {func_df['execution_time'].quantile(0.90):.4f}s")
            print(f"    95th Percentile (P95): {func_df['execution_time'].quantile(0.95):.4f}s")
            print(f"    99th Percentile (P99): {func_df['execution_time'].quantile(0.99):.4f}s")
        else:
            print("    No execution time data for successful invocations.")

        if not cold_starts.empty and not cold_starts['execution_time'].empty:
            print("  --- Cold Start Invocations ---")
            print(f"    Mean Cold Start Time: {cold_starts['execution_time'].mean():.4f}s")
        if not warm_starts.empty and not warm_starts['execution_time'].empty:
            print("  --- Warm Start Invocations ---")
            print(f"    Mean Warm Start Time: {warm_starts['execution_time'].mean():.4f}s")
    else:
        print(f"\nFunction: '{func_name}' - No successful invocations to analyze.")


# --- Plotting Enhancements (Separate Figures for each type) ---

# Figure 1: Individual Function Execution Time Over Time (Using Scatter for clarity)
if not successful_df.empty:
    n_rows_fig1 = len(unique_functions)
    if n_rows_fig1 > 0:
        # Removed sharex=True to allow independent x-axis formatting for clarity
        fig1, axes1 = plt.subplots(n_rows_fig1, 1, figsize=(15, 5 * n_rows_fig1))
        # Ensure axes1 is always an array, even for a single subplot
        if n_rows_fig1 == 1:
            axes1 = [axes1]

        for i, func_name in enumerate(unique_functions):
            ax = axes1[i]
            subset = successful_df[successful_df['function'] == func_name].sort_values(by='timestamp')
            if not subset.empty:
                # Use plot (with markers) for a clearer line. Scatter can also be used.
                ax.plot(subset['timestamp'], subset['execution_time'], marker='o', linestyle='-', markersize=4, label=func_name)

                ax.set_title(f'Execution Time Over Time for "{func_name}"', fontsize=12)
                ax.set_ylabel('Execution Time (seconds)')
                ax.legend()
                ax.grid(True)

                # More flexible X-axis formatting
                locator = mdates.AutoDateLocator(maxticks=5) # Adjust max ticks if needed
                formatter = mdates.DateFormatter('%H:%M:%S') # Display HH:MM:SS
                # For very short runs, consider '%M:%S' or '%S.%f' (seconds and microseconds)
                # If only a few minutes, this might be better: mdates.DateFormatter('%M:%S')

                ax.xaxis.set_major_locator(locator)
                ax.xaxis.set_major_formatter(formatter)
                fig1.autofmt_xdate(rotation=45) # Auto-format and rotate for better fit

        fig1.suptitle('Individual Function Execution Time Trends', fontsize=16, y=1.02)
        fig1.tight_layout(rect=[0, 0.03, 1, 0.98]) # Adjust layout to prevent overlapping titles/labels
        plt.show() # Display this figure


# Figure 2: Overall Function Execution Time Over Time (Combined)
if len(unique_functions) > 1 and not successful_df.empty: # Only if more than one function
    fig2, ax2 = plt.subplots(1, 1, figsize=(15, 8))
    for func in unique_functions:
        subset = successful_df[successful_df['function'] == func].sort_values(by='timestamp')
        if not subset.empty:
            ax2.plot(subset['timestamp'], subset['execution_time'], marker='o', linestyle='-', markersize=4, label=func)
    ax2.set_title('Overall Function Execution Time Over Time (Combined View)')
    ax2.set_xlabel('Timestamp')
    ax2.set_ylabel('Execution Time (seconds)')
    ax2.legend()
    ax2.grid(True)
    ax2.tick_params(axis='x', rotation=45)
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    fig2.tight_layout()
    plt.show() # Display this figure


# Figure 3: Distribution of Execution Times (Histograms)
if not successful_df.empty:
    fig3, ax3 = plt.subplots(1, 1, figsize=(15, 8))

    # Calculate combined min/max for all functions for consistent binning
    all_exec_times = successful_df['execution_time'].dropna()
    if not all_exec_times.empty:
        min_time = all_exec_times.min()
        max_time = all_exec_times.max()
        # Ensure bins are not zero or negative if min/max are too close
        # Use np.linspace for clear bin edges
        bins = np.linspace(min_time, max_time, 40) if max_time > min_time else 10 # More bins for detail

        for func_name in unique_functions:
            func_exec_times = successful_df[successful_df['function'] == func_name]['execution_time'].dropna()
            if not func_exec_times.empty:
                ax3.hist(func_exec_times, bins=bins, alpha=0.6, label=func_name, density=True)

        ax3.set_title('Distribution of Execution Times by Function')
        ax3.set_xlabel('Execution Time (seconds)')
        ax3.set_ylabel('Density')
        ax3.legend()
        ax3.grid(True)
        fig3.tight_layout()
        plt.show() # Display this figure
    else:
        print("No successful execution time data for histogram plot.")


# Figure 4: Cold Start vs. Warm Start Comparison (Boxplot)
if 'is_cold_start' in successful_df.columns and not successful_df['is_cold_start'].dropna().empty:
    fig4, ax4 = plt.subplots(1, 1, figsize=(10, 6))

    cold_start_times = successful_df[successful_df['is_cold_start'] == True]['execution_time'].dropna()
    warm_start_times = successful_df[successful_df['is_cold_start'] == False]['execution_time'].dropna()

    boxplot_data = []
    labels = []

    if not cold_start_times.empty:
        boxplot_data.append(cold_start_times)
        labels.append('Cold Starts')
    if not warm_start_times.empty:
        boxplot_data.append(warm_start_times)
        labels.append('Warm Starts')

    if boxplot_data:
        ax4.boxplot(boxplot_data, labels=labels, patch_artist=True)
        ax4.set_title('Execution Time: Cold vs. Warm Starts')
        ax4.set_ylabel('Execution Time (seconds)')
        ax4.grid(True)
        fig4.tight_layout()
        plt.show() # Display this figure
    else:
        print("Not enough data to generate Cold vs. Warm Starts boxplot.")
else:
    print("Cold start data not available or empty for plotting.")