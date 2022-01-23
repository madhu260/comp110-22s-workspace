"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730475197"

print("Tell me a word you're thinking of")
word: str = str(input("Enter a 5-character word: "))
length_of_word: int = len(word)

if length_of_word != 5 :
    print("Error: Word must contain 5 characters")
    quit()

letter: str = str(input("Enter a single letter: "))
print("Serching for " + letter + " in " + word)

if word[0] == letter:
    print(letter + " found at index 0")
if word[1] == letter:
    print(letter + " found at index 1")
if word[2] == letter:
    print(letter + " found at index 2")
if word[3] == letter:
    print(letter + " found at index 3")
if word[4] == letter:
    print(letter + " found at index 4")
if word[0] != letter and word[1] != letter and word[2] != letter and word[3] != letter and word[4] != letter:
    print("No instances of " + letter + " found in " + word)