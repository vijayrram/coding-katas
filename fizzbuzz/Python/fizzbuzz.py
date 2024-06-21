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

    output = ""
    output += "Fizz" if inp % 3 == 0 else ""
    output += "Buzz" if inp % 5 == 0 else ""

    return output if output else str(inp)


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz(num))
