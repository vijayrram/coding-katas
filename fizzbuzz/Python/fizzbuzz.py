"""FizzBuzz Coding Kata"""

from fizzbuzz_rules import FIZZBUZZ_RULES, apply_rule


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
        output += apply_rule(inp, rule)

    return output if output else str(inp)


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz(num))
