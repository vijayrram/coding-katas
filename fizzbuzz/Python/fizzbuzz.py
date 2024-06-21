"""FizzBuzz Coding Kata"""

FIZZBUZZ_RULES: list[tuple[int, str]] = [
    (3, "Fizz"),
    (5, "Buzz"),
]


def fizzbuzz(inp: int) -> str | int:
    """Helper used to modify input integers to the correct response for the FizzBuzz game.

    Args:
        inp (int): Number to be modified.

    Returns:
        str: Response to be uttered instead.
    """

    if not isinstance(inp, int):
        raise TypeError("Invalid input type.")

    output = ""
    for rule in FIZZBUZZ_RULES:
        output += rule[1] if inp % rule[0] == 0 else ""

    return output if output else str(inp)


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz(num))
