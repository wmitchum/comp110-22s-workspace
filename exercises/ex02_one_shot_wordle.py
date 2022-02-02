"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730329770"

secret: str = "python"
guess: str = input(f"What is your {str(len(secret))}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {str(len(secret))} letters! Try again:") #this line is activated if the user guesses a word of the incorrect length

index_counter: int = 0 #This line defines a variable used to track the index of the secret and guess word
result: str = ""

while index_counter < len(secret):
    if guess[index_counter] == secret[index_counter]:
        result = f"{result} \U0001F7E9" #This line activates if characters of the guess word and secret are word in the same index match
    else:
        character_in_secret: bool = False
        alternate_index: int = 0    #These variables are used to test if the character of the guessed word is anywhere within the secret word
        while character_in_secret != True and alternate_index < len(guess):
            if guess[index_counter] == secret[alternate_index]:
                character_in_secret = True
            else:
                alternate_index = alternate_index + 1
        if character_in_secret == True:
            result = f"{result} \U0001F7E8"
        else: 
            result = f"{result} \U00002B1C"
    index_counter = index_counter + 1 #This iterates to the next character of the guess word to be tested for accuracy.

print(result)
if guess == secret:
    print("Woo! You got it!")
    exit()
else:
    print("Not quite. Play again soon!")
    exit()
