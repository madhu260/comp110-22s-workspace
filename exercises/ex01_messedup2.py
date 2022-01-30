"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730475197"


word: str = input("Enter a  5-character word: ")
length_of_word: int = len(word)

if length_of_word != 5:
    print("Error: Word must contain 5 characters")
    quit()

letter: str = input("Enter a single character: ")
length_of_letter: int = len(letter)

if length_of_letter != 1:
    print("Error: Character must be a single character.")
    quit()

print("Serching for " + letter + " in " + word)

instances = 0

if word[0] == letter:
    print(letter + " found at index 0")
    instances = instances + 1
if word[1] == letter:
    print(letter + " found at index 1")
    instances = instances + 1 
if word[2] == letter:
    print(letter + " found at index 2")
    instances = instances + 1
if word[3] == letter:
    print(letter + " found at index 3")
    instances = instances + 1
if word[4] == letter:
    print(letter + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + letter + " found in " + word)
if instances == 1:
    print(str(instances) + " instance of " + letter + " found in " + word)
else:
    print(str(instances) + " instances of " + letter + " found in " + word)
