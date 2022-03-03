"""Functions to test file ex06/dictionary."""

__author__ = "730475197"

from dictionary import invert, favorite_colors, count


def test_invert_two_same() -> None:
    """When the keys and values are the same"""
    dict_a: dict[str, str] = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f"}
    assert invert(dict_a) == {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f"}


def test_invert_use_1() -> None:
    """Random dictionary given to invert."""
    dict_a: dict[str, str] = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6"}
    assert invert(dict_a) == {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f"}


def test_invert_use_2() -> None:
    """Different random dictionary given to invert."""
    dict_a: dict[str, str] = {"26": "z", "25": "y", "24": "x", "23": "w", "22": "v"}
    assert invert(dict_a) == {"z": "26", "y": "25", "x": "24", "w": "23", "v": "22"}


def test_favorite_colors_empty() -> None:
    """When the dictionary is empty."""
    dict_empty: dict[str, str] = {}
    assert favorite_colors(dict_empty) == ""


def test_favorite_colors_use_1() -> None:
    """Normal usage to find most popular favorite color given a dictionary."""
    dict_colors: dict[str, str] = {"Steph": "pink", "Chris": "blue", "Maddy": "pink", "Eve": "yellow", "Leo": "purple"}
    assert favorite_colors(dict_colors) == "pink"


def test_favorite_colors_use_2() -> None:
    """Normal usage to find most popular favorite color given a different dictionary."""
    dict_colors: dict[str, str] = {"Steph": "blue", "Eve": "purple", "Maddy": "purple", "Leo": "blue", "Chris": "purple"}
    assert favorite_colors(dict_colors) == "purple"


def test_count_empty() -> None:
    """Must return empty dictionary given empty string."""
    list_empty: list[str] = []
    assert count(list_empty) == {}


def test_count_use1() -> None:
    """Normal usage of count, given strings of numbers."""
    list_a: list[str] = ["1", "2", "3", "3", "4", "3", "4"]
    assert count(list_a) == {"1": 1, "2": 1, "3": 3, "4": 2}


def test_count_use2() -> None:
    """Normal usage of count, given strings of letters."""
    list_a: list[str] = ["a", "b", "b", "c", "d", "c", "e"]
    assert count(list_a) == {"a": 1, "b": 2, "c": 2, "d": 1, "e": 1}