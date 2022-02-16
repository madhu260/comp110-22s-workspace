"""Final version of wordle with 6 chances."""


__author__ = "730475197"


def contains_char(word: str, char: str) -> bool:
    """Checks for character in the word."""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Converts answers to emojis."""
    assert len(guess) == len(secret)
    
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i: int = 0

    while i < len(secret):
        if contains_char(secret, guess[i]) is True:
            alt: int = 0
            while i < int(len(secret)) and alt < len(secret):
                if guess[i] == secret[i]:
                    emoji += GREEN_BOX
                    i += 1
                else:
                    if guess[i] == secret[alt]:
                        emoji += YELLOW_BOX
                        i += 1
                    alt += 1
        else:
            emoji += WHITE_BOX
            i += 1
    return emoji


def input_guess(a: int) -> str:
    """Makes sure word is the required length of letters and returns word.""" 
    ans: bool = True
    guess: str = input(f"Enter a {a} character word: ") 
    while ans:
        if len(guess) == a:
            ans = False
        else:
            another_g: str = input(f"That wasn't {a} chars! Try again: ")
            guess = another_g
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = ("codes")
    turn = 1
    while turn < 6:
        print(f"=== Turn {turn}/6 ===")
        guess_word = input_guess(len(secret))
        if guess_word == secret:
            print(f"You won in {turn}/6 turns!")
            print(emojified(guess_word, secret))
            turn = 7
        else:
            print(emojified(guess_word, secret))
            turn += 1
        if turn == 6:
            print(f"=== Turn {turn}/6 ===")
            guess_word = input_guess(len(secret))
            if guess_word != secret:
                print(emojified(guess_word, secret))
                print("X/6 - Sorry, try again tomorrow!")
            else:
                print(emojified(guess_word, secret))
                print(f"You won in {turn}/6 turns!")


if __name__ == "__main__":
    main()

