"""EX06 - Dictionary Functions."""

__author__ = "730329770"


def invert(dic: dict[str, str]) -> dict[str, str]:
    """Swaps Key and Value for each K-V pair in given dictionary."""
    invdic: dict[str, str] = {}
    for key in dic:
        invdic[dic[key]] = key  # This takes the value from the dictionary and adds it as the key to the new dictionary. It then sets it equal to the key of the given list. 
    return invdic


def favorite_color(dic: dict[str, str]) -> str:
    """Returns the most common favorite color in a dictionary of names and asociated favorite colors."""
    color_frequency: dict[str, int] = {}
    most_frequent_color: str = ""
    max_frequency: int = 0
    for person in dic:  # The following under this for loop will create a new dictionary with each color mentioned and how many times it occurs in the oringinal dictionary. 
        if dic[person] in color_frequency:
            color_frequency[dic[person]] += 1
        else:
            color_frequency[dic[person]] = 1
    for color in color_frequency:  # This for in loop evaluates each value in the new dictionary and compares it to the previously largest number. If it is larger, it redefines the max and redefines the color. 
        if color_frequency[color] > max_frequency:
            max_frequency = color_frequency[color]
            most_frequent_color = color
    return most_frequent_color  # This returns the max color. If there are multiple maxes (equal), it returns the first.


def count(a_list: list[str]) -> dict[str, int]:
    """Given a list of strings, this function returns a dictionary with the strings from the list as the key and a value of how many times they occurred in the list."""
    my_dic: dict[str, int] = {}
    for item in a_list:
        if item in my_dic:
            my_dic[item] += 1
        else:
            my_dic[item] = 1
    return my_dic