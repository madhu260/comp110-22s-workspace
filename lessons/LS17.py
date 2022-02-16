"""Test subject example. Sum."""


def sum(xs: list[float]) -> float:
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total