def hello_world(name: str = "World"):
    """
    Greets the user. Maps to GET /hello
    """
    return {"message": f"Hello, {name}!"}, 200


def add_numbers(a: int, b: int):
    """
    Sums two integers. Maps to GET /add
    """
    result = a + b
    return {"result": result}, 200
