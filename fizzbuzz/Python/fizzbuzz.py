"""FizzBuzz Coding Kata"""

from fizzbuzz_rules import FIZZBUZZ_RULES, apply_divisibility_rule


def fizzbuzz(number: int) -> str | int:
    """Helper used to modify input integers to the correct response for the FizzBuzz game.

    Args:
        number (int): Number to be modified.

    Returns:
        str: Response to be uttered instead.
    """

    if not isinstance(number, int):
        raise TypeError("Invalid input type.")

    output = "".join(apply_divisibility_rule(number, rule) for rule in FIZZBUZZ_RULES)

    return output if output else str(number)


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz(num))
