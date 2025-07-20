# functions/hello.py
def handler(params):
    name = params.get("name", "World")
    return f"Hello, {name}!"
