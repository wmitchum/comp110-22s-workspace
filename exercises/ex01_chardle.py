"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730329770"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    quit()
number_of_instances: int = 0
print("Searching for " + single_character + " in " + five_character_word)

if single_character == five_character_word[0]:
    number_of_instances = number_of_instances + 1
    print(single_character + " found at index 0")
if single_character == five_character_word[1]:
    number_of_instances = number_of_instances + 1
    print(single_character + " found at index 1")
if single_character == five_character_word[2]:
    number_of_instances = number_of_instances + 1
    print(single_character + " found at index 2")
if single_character == five_character_word[3]:
    number_of_instances = number_of_instances + 1
    print(single_character + " found at index 3")
if single_character == five_character_word[4]:
    number_of_instances = number_of_instances + 1
    print(single_character + " found at index 4")

if number_of_instances > 1:
    print(str(number_of_instances) + " instances of " + single_character + " found in " + five_character_word)
    quit()
if number_of_instances == 1:
    print(str(number_of_instances) + " instance of " + single_character + " found in " + five_character_word)
    quit()
else:
    print ("No instances of " + single_character + " found in " + five_character_word)
    quit()