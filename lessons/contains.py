"""Example of writing a function to search a list."""

def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle found in haystack."""
    for item in haystack:
        if item == needle:
            return True
    return False


# Returns True iff needle is found in haystack