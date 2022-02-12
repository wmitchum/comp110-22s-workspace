"""EX03 - Structured Wordle."""

__author__ = "730329770"


def contains_char(secret: str, char: str) -> bool:
    """This function searches for character in secret and returns True if character is found in secret."""
    assert len(char) == 1
    i: int = 0
    char_in_secret: bool = False
    while i < len(secret):
        if char == secret[i]:
            char_in_secret = True
            return char_in_secret
        else:
            i += 1
    return char_in_secret


def emojified(guess: str, secret: str) -> str:
    """This function compares the guess word to the secret word by evaluating each index of the guess word as compared to the secret word and outputs the appropriate colored emojis."""
    assert len(guess) == len(secret)
    result: str = ""  # This variable will store the emoji boxes.
    i: int = 0  # This is our counter to compare each index of guess to secret.
    while i < len(secret):
        if guess[i] == secret[i]:
            result = f"{result}\U0001F7E9"
        else:
            if contains_char(secret, guess[i]) is True:
                result = f"{result}\U0001F7E8"
            else:
                result = f"{result}\U00002B1C"
        i += 1  # This iterates our index and therefore tests the next index in guess once we have concatinated our blank string.
    return result


def input_guess(expected_length: int) -> str:
    """This function ensures the player chooses a guess equal to the length of the secret word specified in the game.""" 
    guess: str = input(f"Enter a {str(expected_length)}-character word :")  # By using an f-string, expected_length can be any integer.
    while len(guess) != expected_length:
        guess = input(f"That wasn't {str(expected_length)} chars! Try again :")  # This loop will continue until the user enters a guess of proper character length.
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_number: int = 1  # This variable will keep track of how many turns the player has left.

    while turn_number < 7:
        print (f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret))

