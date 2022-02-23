"""Tests functions from utils."""
__author__ = "730475197"

from utils import only_evens, sub, concat

randlist1: list = [2, 3, 4] 
randlist2: list = [5, 6, 7, 8, 9]
empty: list[int] = []


def test_only_evens_just_odds() -> None:
    xs: list[int] = [3, 5, 7]
    assert only_evens(xs) == []


def test_only_evens_use_1() -> None:
    assert only_evens(randlist1) == [2, 4]


def test_only_evens_use_2() -> None:
    assert only_evens(randlist2) == [6, 8]


def test_sub_empty_list() -> None:
    assert sub(empty, -1, 2) == []


def test_sub_use_1() -> None:
    assert sub(randlist1, 0, 2) == [2, 3]


def test_sub_use_2() -> None:
    assert sub(randlist2, 2, 5) == [7, 8, 9]


def test_concat_empty_lists() -> None:
    assert concat(empty, empty) == []


def test_concat_use_1() -> None:
    assert concat(randlist1, randlist2) == [2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_use_2() -> None:
    list_a: list = [10, 20, 30]
    list_b: list = [70, 60, 50]
    assert concat(list_a, list_b) == [10, 20, 30, 70, 60, 50]