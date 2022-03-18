def count_letters(lines: list[str]) -> dict[str, int]:
    """Count frequencies of all letters in a list of strings."""
    counts: dict[str, int] = {}
    characters: list[str] = []
    i = 0
    while i < len(lines):
        for x in lines[i]:
            characters.append(x)
        i +=1
    j = 0
    while j <  
    # loop through all lines
    # for each line, loop through every character
    # Tally character into the counts dictionary
    # Tally only letters! No numbers or punctuation.
    return counts


# def tally(key: str, value: int):
#     """ ."""
#     i: int = 0
#     while i < len(read_file(#shakespeare.txt))
# #    file: TextIOWrapper = open(filename, "r", encoding="utf8")
#         if key in read_file()
#             value += 1
#             i += 1
#     return value
