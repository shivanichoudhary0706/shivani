def handler(event):
    count = event.get("iterations", 1000000)
    total = 0
    for i in range(count):
        total += i*i
    return f"CPU loop done. Total: {total}"
