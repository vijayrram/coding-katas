"""FizzBuzz Coding Kata"""

from fizzbuzz_rules import FIZZBUZZ_RULES, apply_rule, apply_rule2


def fizzbuzz2(number: int) -> str | int:
    """Helper used to modify input integers to the correct response for the FizzBuzz game version 2.

    Args:
        number (int): Number to be modified.

    Returns:
        str: Response to be uttered instead.
    """

    if not isinstance(number, int):
        raise TypeError("Invalid input type.")

    output = "".join(apply_rule2(number, rule) for rule in FIZZBUZZ_RULES)
    output += "".join(apply_rule(number, rule) for rule in FIZZBUZZ_RULES)

    return output if output else str(number)


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz2(num))
