def cpu_burn(iterations: int):
    result = 0
    for i in range(iterations):
        result += i * i
    return result
