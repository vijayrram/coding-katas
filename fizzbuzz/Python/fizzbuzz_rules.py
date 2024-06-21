"""Rules for FizzBuzz."""

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
