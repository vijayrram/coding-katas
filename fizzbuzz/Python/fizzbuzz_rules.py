"""Rules for FizzBuzz."""

from typing import Callable, NamedTuple, TypeAlias


FizzBuzzRules: TypeAlias = list[Callable[[int], str]]


class FizzBuzzRule(NamedTuple):
    """Class used to define FizzBuzz rules."""

    divisor: int
    response: str


FIZZBUZZ_RULES: list[FizzBuzzRule] = [
    FizzBuzzRule(divisor=3, response="Fizz"),
    FizzBuzzRule(divisor=5, response="Buzz"),
]


def apply_divisibility_rule(number: int) -> str:
    """Helper function used to apply the FizzBuzz divisibility rule to the input value.

    Args:
        number (int): Input value.
        rule (FizzBuzzRule): Rule to be applied.

    Returns:
        str: Response to be returned.
    """

    return "".join(rule.response if number % rule.divisor == 0 else "" for rule in FIZZBUZZ_RULES)


def apply_contains_rule(number: int) -> str:
    """Helper function used to apply the FizzBuzz contains rule to the input value.

    Args:
        number (int): Input value.
        rule (FizzBuzzRule): Rule to be applied.

    Returns:
        str: Response to be returned.
    """

    return "".join(
        rule.response
        if str(rule.divisor) in str(number)
        else "" for rule in FIZZBUZZ_RULES
    )



def fizzbuzz_response_generator(fizzbuzz_rules: FizzBuzzRules) -> Callable[[int], str]:
    """Factory method for creating FizzBuzz responders.

    Args:
        fizzbuzz_rules (FizzBuzzRules): List of rules to be applied.

    Returns:
        Callable[[int], str]: The generated responder.
    """

    def inner(number: int) -> str:
        """Responder to be returned.

        Args:
            number (int): Number on which the rules should be applied.

        Returns:
            str: Reponse obtained after applying the rules.
        """

        if not isinstance(number, int):
            raise TypeError("Invalid input type.")

        output = "".join(rule(number) for rule in fizzbuzz_rules)

        return output if output else str(number)

    return inner


fizzbuzz2 = fizzbuzz_response_generator([apply_contains_rule, apply_divisibility_rule])
