"""Wordle Prompt for Comp110"""

__author__ = "730765505"


def input_guess(secret_word_len: int) -> str:
    i: int = 0
    guess = input(f"Enter a {secret_word_len} letter word: ")
    while i == 0:
        if len(guess) != secret_word_len:
            guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        else:
            i = 1
    return guess


def contains_char(input: str, char: str) -> bool:
    """Checks if there is char in input"""
    assert len(char) == 1
    i: int = 0
    char_found: bool = False
    while i < len(input):
        if input[i] == char:
            char_found = True
        i += 1
    return char_found


def emojified(guess: str, secret: str) -> str:
    """Checks if two strings have an emoji"""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    response: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            response = response + green_box
        elif contains_char(input=secret, char=guess[i]):
            response = response + yellow_box
        else:
            response = response + white_box
        i += 1
    return response


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        response: str = emojified(guess=guess, secret=secret)
        print(response)
        if response == "\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9":
            print(f"You won in {turn}/6 turns!")
            turn = 9
        turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
