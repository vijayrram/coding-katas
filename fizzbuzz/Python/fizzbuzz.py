"""Script for building FizzBuzz responders."""

from typing import Callable, NamedTuple


class FizzBuzzResponder(NamedTuple):
    """Class used to define FizzBuzz responses."""

    digit: int
    response: str

    def evaluate(self, number: int, func: Callable[[int, int], bool]) -> str:
        """Method to evaluate a number according to a rule and respond appropriately.

        Args:
            number (int): Number to be evaluated.
            func (Callable[[int, int], bool]): Function used to evaluate the number

        Returns:
            str: Evaluated response.
        """

        return self.response if func(number, self.digit) else ""


class FizzBuzz:
    """Class containing methods to build a FizzBuzz responder."""

    def __init__(self):
        self.rules: list[Callable[[int], str]] = []
        self.responders: list[FizzBuzzResponder] = []

    def add_response(self, digit: int, response: str) -> None:
        """Method used to add a response used when checking the number against the passed digit.

        Args:
            digit (int): Digit to be affected
            response (str): Response to be said instead
        """

        self.responders.append(FizzBuzzResponder(digit=digit, response=response))

    def add_rule(self, func: Callable[[int, int], bool]) -> None:
        """Factory method for adding rules to be applied to the numbers. Rules are executed in the
        order they are added.

        Args:
            func (Callable[[int, int], bool]): Function used to check if rule should be applied.
        """

        def inner(number: int) -> str:
            """Rule to be returned.

            Args:
                number (int): Number on which the rule is applied.

            Returns:
                str: Response provided after the rule is applied.
            """

            return "".join(responder.evaluate(number, func) for responder in self.responders)

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
fizzbuzz.add_rule(lambda number, divisor: number % divisor == 0)

fizzbuzz2 = FizzBuzz()
fizzbuzz2.add_response(digit=3, response="Fizz")
fizzbuzz2.add_response(digit=5, response="Buzz")
fizzbuzz2.add_rule(lambda number, digit: str(digit) in str(number))
fizzbuzz2.add_rule(lambda number, divisor: number % divisor == 0)
