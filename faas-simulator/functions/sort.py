# functions/sort.py
def handler(params):
    import random
    size = params.get("size", 10000)
    data = [random.randint(0, 10000) for _ in range(size)]
    sorted_data = sorted(data)
    return "Sorting completed"
