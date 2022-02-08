"""Wordle but you only get one shot."""
__author__ = "730475197"

secret: str = ("python")


word: str = input(f"What is your {len(secret)}-letter guess? ")
length_of_word: int = len(word)


while len(word) != len(secret):
    word = input(f"That was not {len(secret)} letters! Try again: ")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

if word == secret:
    print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
    print("Woo! You got it!")
else:
    emoji: str = ""
    i: int = 0
    while i < int(len(secret)):
        if word[i] == secret[i]:
            emoji += GREEN_BOX 
            i += 1
        else:
            other_position: bool = False
            alt = 0
            while not (other_position is True) and alt < len(secret):
                if word[i] == secret[alt]:
                    other_position = True
                else: 
                    alt += 1
            if other_position:                              # if other_position == True:
                emoji += YELLOW_BOX
                i += 1  
            if not other_position:                          # else
                emoji += WHITE_BOX 
                i += 1

    print(emoji)
    print("Not quite. Play again soon!")