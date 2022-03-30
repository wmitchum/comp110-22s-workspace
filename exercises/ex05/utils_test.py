"""EX05 - 'list' Utility Functions Test."""

__author__ = "730329770"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:  
    """This ensures an empty list returns an empty list."""
    assert only_evens([]) == []


def test_only_evens_all_evens() -> None:
    """Reterns all numbers of all even list."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_only_evens_all_odds() -> None:
    """Returns no numbers of all odd list."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_practical() -> None:  
    """Tests a scenario for which we intend to use the function."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_sub_empty() -> None:
    """Tests for empty list."""
    assert sub([], 0, 0) == []


def test_sub_start_too_big() -> None:
    """Tests for too large of a starting bound."""
    assert sub([1, 3, 4, 7], 4, 5) == []  # An empty list should be returned if the start bound is larger than the greatest index


def test_sub_end_too_small() -> None:
    """Tests for too small of an ending bound."""
    assert sub([1, 3, 4, 7], 1, -1) == []  # An empty list should be returned if the end bound is 0 or less


def test_sub_start_too_small() -> None:
    """Tests for too small of a starting bound."""
    assert sub([1, 3, 4, 7], -1, 4) == [1, 3, 4, 7]  # An empty list should be returned if the end bound is 0 or less


def test_sub_same_bounds() -> None:
    """Tests for the same bounds."""  # This ensures that the upper bound is never included
    assert sub([1, 2, 3], 2, 2) == []


def test_sub_practical() -> None:
    """Tests for scenario in which we intend to use the function."""
    assert sub([10, 20, 30, 40], 0, 3) == [10, 20, 30]


def test_sub_uncronilogical() -> None:
    """Makes sure size of list items not being compared, but rather indeces."""  # Assuring that the function is gagueing indecies and not the size of the list values.
    assert sub([20, 3, 4, 99], 1, 3) == [3, 4]


def test_concat_empty_lists() -> None:
    """Tests for two empty lists."""  # If both lists are empty, we should get an empty list.
    assert concat([], []) == []


def test_concat_practical_use() -> None: 
    """Tests for case in which we intend to use function."""
    assert concat([10, 20, 30], [10, 20, 30]) == [10, 20, 30, 10, 20, 30]


def test_concat_one_empty_list_a() -> None:  
    """Tests for concatinationg to an empty list_a."""  # If list_a is empty, we should see the contents of list b.
    assert concat([], [1, 2, 3]) == [1, 2, 3]