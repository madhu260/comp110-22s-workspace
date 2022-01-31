"""Wordle but you only get one shot."""
__author__ = "730475197"

secret: str = ("python")


word: str = input(f"What is your {len(secret)}-letter guess? ")
length_of_word: int = len(word)


while len(word) != len(secret):
    word = input(f"That was not {len(secret)} letters! Try again: ")


WHITE_BOX: str = "\U00002B1C "
GREEN_BOX: str = "\U0001F7E9 "
YELLOW_BOX: str = "\U0001F7E8 "

if word == secret:
    print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
    print("Woo! You got it!")
else:
    emoji: str = ""
    i = 0
    while i < len(secret):
        if word[i] == secret[i]:
            emoji += GREEN_BOX 
            i += 1
        if word[i] != secret[i]:
            other_position: bool = False
            alt = 0
            while not (other_position is True) and alt < len(secret):
                if word[i] == secret[alt]:
                    emoji += YELLOW_BOX 
                    other_position = True
                    i += 1
                elif word[i] != secret[alt] and alt == len(secret) - 1:
                    emoji += WHITE_BOX 
                    i += 1
                    break
                else: 
                    alt += 1
    print(emoji)
    print("Not quite. Play again soon!")