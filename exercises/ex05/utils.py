"""EX05 - 'list' Utility Functions."""

__author__ = "730329770"

import pytest


def only_evens(nums: list[int]) -> list[int]:
    """Outputs a list of even numbers from a given list of integers."""
    evens: list[int] = list()  # This is our empty list to which we will append all even numbers in nums
    for item in nums: 
        if item % 2 == 0:  # This will only return for even numbers
            evens.append(item)  # This appends even numbers to our empty list
    return evens


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Outputs a sublist of a list within specified indece bounds."""
    nums_in_bounds: list[int] = list()
    i: int = start  # This sets the starting range equal to the lower limit
    if start < 0:
        i == 0
    if end >= len(a_list) and len(a_list) > 0:
        end == a_list[(len(a_list) - 1)]
    while i < end and i < len(a_list):  # This ensures the upper bound is not included while counting through the specified range
        nums_in_bounds.append(a_list[i])
        i += 1
    return nums_in_bounds


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Concatinates two lists in cronilogical order."""
    for item in list_b:
        list_a.append(item)
    return list_a