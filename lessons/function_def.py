"""An example function definition."""


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b: 
        return a
    else:
        return b

print(my_max(10+1, 10))

# Line number 4 is the signature ("contract") line. 
# Line number 5 is the docstring describing the function
# The rest is the body block
#Line 11 actually makes something happen, otherwise nothing would when you run the code.