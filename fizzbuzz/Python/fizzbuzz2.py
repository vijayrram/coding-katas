"""FizzBuzz Coding Kata"""

from typing import Callable, TypeAlias
from fizzbuzz_rules import apply_contains_rule, apply_divisibility_rule

FizzBuzzRules: TypeAlias = list[Callable[[int], str]]


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


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz2(num))
