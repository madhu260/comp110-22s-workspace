# def change_and_check(x, nums):
#     """doc."""

#     if x < 0:
#         return 0
        
#     i = 0
#     while i < (len(nums)):
#         nums[i] += x
#         i += 1
        
#     i = 0
#     while i < (len(nums)):
#         if nums[i] == x:
#             return 0
#         i += 1
#     return x - 1


# def main() -> None:
#     num_1 = 0
#     list_1 = [1, 2, num_1]
#     list_1.append(change_and_check(2, list_1))
#     list_1.append(change_and_check(3, list_1))
#     print(list_1)


# main()

# create a dictionary
# marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }

# element = marks.pop('Chemistry')

# print(marks)

# Output: Popped Marks: 72


def repeat(word:str, a: int) -> str:
    """repeats."""
    new_word: str = ""
    letter: int = 0
    while len(new_word) < (len(word) * a):
        i: int = 0
        while i < a:
            new_word += word[letter]
            i += 1
        letter+=1
    return new_word

print(repeat("tar", 3))
