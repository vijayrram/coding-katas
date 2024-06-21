"""FizzBuzz Coding Kata"""

from typing import NamedTuple


class FizzBuzzRule(NamedTuple):
    """Class used to define FizzBuzz rules."""

    divisor: int
    response: str


FIZZBUZZ_RULES: list[FizzBuzzRule] = [
    FizzBuzzRule(divisor=3, response="Fizz"),
    FizzBuzzRule(divisor=5, response="Buzz"),
]


def apply_rule(inp: int, rule: FizzBuzzRule) -> str:
    """Helper function used to apply the FizzBuzz rule to the input value.

    Args:
        inp (int): Input value.
        rule (FizzBuzzRule): Rule to be applied.

    Returns:
        str: Response to be returned.
    """

    return rule.response if inp % rule.divisor == 0 else ""


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
