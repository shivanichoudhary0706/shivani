def handler(event):
    size = event.get("size", 1000000)
    data = [i for i in range(size)]
    return f"Allocated list of size: {len(data)}"
