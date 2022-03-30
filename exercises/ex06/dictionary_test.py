"""EX06 - Dictionary Functions Testing."""

__author__ = "730329770"


from dictionary import invert, count, favorite_color


def test_invert_empty() -> None:
    """This test insures an empty dictionary returns an empty dictionary."""
    assert invert({}) == {}


def test_invert_normal_use() -> None:
    """Ensures a properly returned dictionary with all unique keys."""
    assert invert({"a": "apple", "b": "boy", "c": "cat"}) == {"apple": "a", "boy": "b", "cat": "c"}


def test_invert_some_keys_are_values() -> None:
    """Duble checks for errors with dictionaries that have some K-V pairs that are the same string."""
    assert invert({"ant": "ant", "b": "boy", "c": "cat"}) == {"ant": "ant", "boy": "b", "cat": "c"}


def test_favorite_color_empty() -> None:
    """This returns an empty string if given an empty list."""
    assert favorite_color({}) == ""


def test_favorite_color_clear_max() -> None:
    """This will test a dictionary we intend to use this function for with a clear most frequent color."""
    assert favorite_color({"wes": "red", "nolan": "red", "jim": "red", "jack": "white", "khayden": "orange", "connor": "orange"}) == "red"


def test_favorite_color_two_maxes() -> None:
    """This will return the first max if there are two."""
    assert favorite_color({"wes": "red", "nolan": "red", "jim": "red", "jack": "white", "khayden": "orange", "connor": "orange", "matt": "orange"}) == "red"


def test_count_empty() -> None:
    """This returns an empty dictionary if the list is empty."""
    assert count([]) == {}


def test_count_all_same_values() -> None:
    """This should return a dictionary of keys with all of the same values."""
    assert count(["one", "two", "three", "four"]) == {"one": 1, "two": 1, "three": 1, "four": 1}


def test_count_duplicate_items_in_a_list() -> None:
    """This tests the intended use of the function using a list with repeated strings."""
    assert count(["one", "one", "two", "three", "four", "four"]) == {"one": 2, "two": 1, "three": 1, "four": 2}