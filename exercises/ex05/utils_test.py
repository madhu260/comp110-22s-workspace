"""Tests functions from ex05/utils."""
__author__ = "730475197"

from utils import only_evens, sub, concat

randlist1: list[int] = [2, 3, 4] 
randlist2: list[int] = [5, 6, 7, 8, 9]
empty: list[int] = []


def test_only_evens_just_odds() -> None:
    """Only odd numbers are inputed."""
    xs: list[int] = [3, 5, 7]
    assert only_evens(xs) == []


def test_only_evens_use_1() -> None:
    """General use tested using a list with generic numbers."""
    assert only_evens(randlist1) == [2, 4]


def test_only_evens_use_2() -> None:
    """General use tested again with similarly generic numbers."""
    assert only_evens(randlist2) == [6, 8]


def test_sub_empty_list() -> None:
    """An empty list is given."""
    assert sub(empty, -1, 2) == []


def test_sub_use_1() -> None:
    """General use tested using a generic list, with normal range."""
    assert sub(randlist1, 0, 2) == [2, 3]


def test_sub_use_2() -> None:
    """General use tested again, using a generic list and normal range."""
    assert sub(randlist2, 2, 5) == [7, 8, 9]


def test_concat_empty_lists() -> None:
    """Empty list is given."""
    assert concat(empty, empty) == []


def test_concat_use_1() -> None:
    """Two generic lists are combined and tested."""
    assert concat(randlist1, randlist2) == [2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_use_2() -> None:
    """Different two lists are given and tested."""
    list_a: list[int] = [10, 20, 30]
    list_b: list[int] = [70, 60, 50]
    assert concat(list_a, list_b) == [10, 20, 30, 70, 60, 50]