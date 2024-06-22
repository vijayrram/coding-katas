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


def apply_divisibility_rule(number: int, rule: FizzBuzzRule) -> str:
    """Helper function used to apply the FizzBuzz divisibility rule to the input value.

    Args:
        number (int): Input value.
        rule (FizzBuzzRule): Rule to be applied.

    Returns:
        str: Response to be returned.
    """

    return rule.response if number % rule.divisor == 0 else ""


def apply_contains_rule(number: int, rule: FizzBuzzRule) -> str:
    """Helper function used to apply the FizzBuzz contains rule to the input value.

    Args:
        number (int): Input value.
        rule (FizzBuzzRule): Rule to be applied.

    Returns:
        str: Response to be returned.
    """

    return rule.response if str(rule.divisor) in str(number) else ""
