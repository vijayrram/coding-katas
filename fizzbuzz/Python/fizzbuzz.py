"""Rules for FizzBuzz."""

from typing import Callable, NamedTuple, TypeAlias


class FizzBuzz:
    """Class containing methods to create a FizzBuzz game."""

    FizzBuzzCondition: TypeAlias = Callable[[int, int], bool]
    FizzBuzzRule: TypeAlias = Callable[[int], str]
    FizzBuzzResponder: TypeAlias = Callable[[int], str]

    class FizzBuzzResponse(NamedTuple):
        """Class used to define FizzBuzz responses."""

        divisor: int
        response: str

    RESPONSES: list[FizzBuzzResponse] = []

    @classmethod
    def add_response(cls, digit: int, response: str) -> None:
        """Method used to add a FizzBuzz response

        Args:
            digit (int): Digit to be affected
            response (str): Response to be said instead
        """

        cls.RESPONSES.append(cls.FizzBuzzResponse(divisor=digit, response=response))

    @classmethod
    def generate_rule(cls, func: FizzBuzzCondition) -> FizzBuzzRule:
        """Factory method for creating FizzBuzz rules.

        Args:
            func (FizzBuzzCondition): Function used to check if rule should be applied.

        Returns:
            FizzBuzzRule: The generated rule.
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
                for rule in cls.RESPONSES
            )

        return inner

    @staticmethod
    def generate_responder(fizzbuzz_rules: list[FizzBuzzRule]) -> FizzBuzzResponder:
        """Factory method for creating FizzBuzz responders.

        Args:
            fizzbuzz_rules (list[FizzBuzzRule]): List of rules to be applied.

        Returns:
            FizzBuzzResponder: The generated responder.
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


divisibility_rule = FizzBuzz.generate_rule(lambda a, b: a % b == 0)
contains_rule = FizzBuzz.generate_rule(lambda a, b: str(b) in str(a))

fizzbuzz = FizzBuzz.generate_responder([divisibility_rule])
fizzbuzz2 = FizzBuzz.generate_responder([contains_rule, divisibility_rule])
