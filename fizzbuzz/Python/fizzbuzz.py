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

    def __init__(self):
        self.rules: list[self.FizzBuzzRule] = []
        self.responses: list[self.FizzBuzzResponse] = []

    def add_response(self, digit: int, response: str) -> None:
        """Method used to add a FizzBuzz response

        Args:
            digit (int): Digit to be affected
            response (str): Response to be said instead
        """

        self.responses.append(self.FizzBuzzResponse(divisor=digit, response=response))

    def add_rule(self, func: FizzBuzzCondition) -> FizzBuzzRule:
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
                for rule in self.responses
            )

        self.rules.append(inner)

    def __call__(self, number: int) -> str:
        """Method used to process numbers as per the rules defined.

        Args:
            number (int): Number on which the rules should be applied.

        Returns:
            str: Reponse obtained after applying the rules.
        """

        if not isinstance(number, int):
            raise TypeError("Invalid input type.")

        output = "".join(rule(number) for rule in self.rules)

        return output if output else str(number)


fizzbuzz = FizzBuzz()
fizzbuzz.add_response(digit=3, response="Fizz")
fizzbuzz.add_response(digit=5, response="Buzz")
fizzbuzz.add_rule(lambda a, b: a % b == 0)

fizzbuzz2 = FizzBuzz()
fizzbuzz2.add_response(digit=3, response="Fizz")
fizzbuzz2.add_response(digit=5, response="Buzz")
fizzbuzz2.add_rule(lambda a, b: str(b) in str(a))
fizzbuzz2.add_rule(lambda a, b: a % b == 0)
