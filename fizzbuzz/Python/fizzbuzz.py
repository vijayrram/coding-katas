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

    if inp % 3 == 0:
        return "Fizz"

    if inp % 5 == 0:
        return "Buzz"

    return str(inp)


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz(num))
