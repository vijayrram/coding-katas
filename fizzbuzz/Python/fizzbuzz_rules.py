"""Rules for FizzBuzz."""

from typing import Callable, NamedTuple, TypeAlias


FizzBuzzRuleApplier: TypeAlias = Callable[[int], str]
FizzBuzzRules: TypeAlias = list[FizzBuzzRuleApplier]
FizzBuzzCondition: TypeAlias = Callable[[int, int], bool]


class FizzBuzzRule(NamedTuple):
    """Class used to define FizzBuzz rules."""

    divisor: int
    response: str


FIZZBUZZ_RULES: list[FizzBuzzRule] = [
    FizzBuzzRule(divisor=3, response="Fizz"),
    FizzBuzzRule(divisor=5, response="Buzz"),
]

def fizzbuzz_rule_generator(func: FizzBuzzCondition) -> FizzBuzzRuleApplier:
    """Factory method for creating FizzBuzz rules.

    Args:
        func (Callable[[int, int], bool]): Function used to check if rule should be applied.

    Returns:
        Callable[[int], str]: The generated rule.
    """

    def inner(number: int) -> str:
        """Rule to be returned.

        Args:
            number (int): Number to be acted on.

        Returns:
            str: Response provided after the rule is applied.
        """

        return "".join(
            rule.response if func(number, rule.divisor) else ""
            for rule in FIZZBUZZ_RULES
        )

    return inner


def fizzbuzz_response_generator(fizzbuzz_rules: FizzBuzzRules) -> FizzBuzzRuleApplier:
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


divisibility_rule = fizzbuzz_rule_generator(lambda a, b: a % b == 0)
contains_rule = fizzbuzz_rule_generator(lambda a, b: str(b) in str(a))

fizzbuzz = fizzbuzz_response_generator([divisibility_rule])
fizzbuzz2 = fizzbuzz_response_generator([contains_rule, divisibility_rule])
