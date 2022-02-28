"""A list of functions to be tested."""


def only_evens(a_list: list[int]) -> list[int]:
    """Returns even numbers only given a list of numbers."""
    xs: list[int] = list()
    for x in a_list:
        if (x % 2) == 0:
            xs.append(x)
    return xs


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Given list of ints, return a list that has gives only the numbers between start (including) and end index."""
    xs: list[int] = list()
    if x < 0:
        x = 0
    if (len(a_list) == 0) or (y <= 0) or (x > len(a_list)):
        return []
    if y > len(a_list):
        y = (len(a_list))
    while (x < y):
        xs.append(a_list[x])
        x += 1
    return xs


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Combines two lists together into one."""
    combined: list[int] = list()
    for x in list_one:
        combined.append(x)
    for x in list_two:
        combined.append(x)
    return combined
