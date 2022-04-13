def add(x: int, y: int = 0, z: int = 0) -> int:
    """Doc."""
    if y == 0:
        y = 1
    return x + y


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))