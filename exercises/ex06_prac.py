"""work"""

my: dict[str, str] = {"Steph": "blue", 'carol': 'green', 'emily': 'pink', 'jon': 'pink', "eng": "pink", "math": "blue", "cpr": "blue"}


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


print(favorite_colors(my))
