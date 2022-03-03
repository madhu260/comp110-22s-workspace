"""Misc functions in relations to dictionary."""

__author__ = "730475197"


def invert(dic_1: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of given dictionary."""
    inverted: dict[str, str] = {}
    keys: list[str] = []
    i: int = 0
    for key in dic_1:
        keys.append(key)
    for key in dic_1:
        count: int = 0
        for x in keys:
            if dic_1[key] == dic_1[x]:
                count += 1
            else:
                i += 1
        if count > 1:
            raise KeyError
        inverted[dic_1[key]] = key
    return inverted


def favorite_colors(dic_a: dict[str, str]) -> str:
    """Returns most favorite color"""
    colors: list[str] = []                          # list with colors
    for key in dic_a:                           
        colors.append(dic_a[key])                   # list with colors
    freq: dict[str, int] = {}                       # freq(value) of color(key)
    for x in colors:                                # items in colors
        i: int = 0                                  # next color in list
        count: int = 0                              # number of times the color appeared
        while i < len(colors):
            if x == colors[i]:                      # if the item is also in colors, add to count
                count += 1
                i += 1
            else:                                   # move on to next item
                i += 1
        freq[x] = count
    biggest_color: str = ""
    value_of_freq: list[int] = []
    for key_2 in freq:
        value_of_freq.append(freq[key_2])
    big_numb: int = 0
    for y in value_of_freq:
        if y > big_numb:
            big_numb = y
    for z in freq:
        if freq[z] == big_numb:
            biggest_color = z
    return biggest_color


def count(list_a: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}                       
    for x in list_a:
        i: int = 0  
        j: int = 0
        while i < len(list_a):
            if x == list_a[i]:
                j += 1
                i += 1
            else:
                i += 1
        freq[x] = j
    return freq
