"""
Custom worldle game for CS 110
"""

__author__ = "730765505"


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        quit()


def input_letter() -> str:
    letter = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        quit()


def contains_char(word: str, char: str) -> None:
    print("Searching for " + char + " in " + word)
    count: int = 0
    for i in range(len(word)):
        if word[i] == char:
            print(char + " found at index " + str(i))
            count += 1
    if count == 0:
        print("No instances of " + char + " found in " + word)
    else:
        print(str(count) + " instances of " + char + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), char=input_letter())


if __name__ == "__main__":
    main()
