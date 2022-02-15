"""EX03 - Structured Wordle."""

__author__ = "730329770"


def contains_char(secret: str, char: str) -> bool:
    """This function searches for character in secret and returns True if character is found at any index in secret."""
    assert len(char) == 1  # We assume the caller will enter a single character. 
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
    assert len(guess) == len(secret)  # We can assume the calle will provide a guess the same length as the secret word. 
    result: str = ""  # This variable will store the emoji boxes.
    i: int = 0  # This is our counter to compare each index of guess to secret.
    while i < len(secret):
        if guess[i] == secret[i]:
            result = f"{result}\U0001F7E9"  # This will concatinate a green box into the empty string. 
        else:
            if contains_char(secret, guess[i]) is True:
                result = f"{result}\U0001F7E8"  # This will concatinate a yellow box into the empty string. 
            else:
                result = f"{result}\U00002B1C"  # This will concatinate a white box into the empty string. 
        i += 1  # This iterates our index and therefore tests the next index in guess once we have concatinated our blank string.
    return result


def input_guess(expected_length: int) -> str:
    """This function ensures the player chooses a guess equal to the length of the secret word specified in the game.""" 
    guess: str = input(f"Enter a {str(expected_length)} character word: ")  # By using an f-string, expected_length can be any integer.
    while len(guess) != expected_length:
        guess = input(f"That wasn't {str(expected_length)} chars! Try again: ")  # This loop will continue until the user enters a guess of proper character length.
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_number: int = 1  # This variable will keep track of how many turns the player has left.
    victory: bool = False  # This will terminate the game when set equal to True

    while turn_number < 7 and victory is not True:
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret))  # calls input guess 
        print(emojified(guess, secret))
        if guess == secret: 
            print(f"You won in {turn_number}/6 turns!")
            victory = True  # This causes the function to terminate if the word is correctly guessed in the alotted number of turns.
        else:
            turn_number += 1  # This will iterate the number of turns
    if victory is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()