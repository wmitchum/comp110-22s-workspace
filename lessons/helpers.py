"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to power of n."""
    return x ** n


# Idiom for making a module able to run as a program
# or have its global definition imported
if __name__ == "__main__":
    main()