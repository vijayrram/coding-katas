"""FizzBuzz Coding Kata"""

def fizzbuzz(inp: int) -> str:
    """Helper used to modify input integers to the correct response for the FizzBuzz game.

    Args:
        inp (int): Number to be modified.

    Returns:
        str: Response to be uttered instead.
    """

    if not isinstance(inp, int):
        raise TypeError("Invalid input type.")

    return str(inp)
