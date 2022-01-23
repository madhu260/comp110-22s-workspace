"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730475197"


word: str = "hello"

print("Can you guess the 5 letter word I'm thinking of?")
guess_1: str = str(input("What do you think it is? "))

if word == guess_1:
    print("Great job! You got it.")
else:
    if word[0] == guess_1[0]:
        print("The letter " + word[0] + " is in the right spot")
    if word[1] == guess_1[1]:
        print("The letter " + word[1] + " is in the right spot")
    if word[2] == guess_1[2]:
        print("The letter " + word[2] + " is in the right spot")
    if word[3] == guess_1[3]:
        print("The letter " + word[3] + " is in the right spot")
    if word[4] == guess_1[4]:
        print("The letter " + word[4] + " is in the right spot")
