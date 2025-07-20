# functions/sort.py
import random
def sort(data: list):
    sorted_data = sorted(data)
    # Return a subset as the full list might be too large for logs
    return {"first_five": sorted_data[:5], "last_five": sorted_data[-5:]}
