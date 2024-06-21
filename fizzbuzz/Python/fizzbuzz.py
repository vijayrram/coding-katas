"""FizzBuzz Coding Kata"""

FIZZBUZZ_RULES: list[tuple[int, str]] = [
    (3, "Fizz"),
    (5, "Buzz"),
]


def apply_rule(inp: int, rule: tuple[int, str]) -> str:
    """Helper function used to apply the FizzBuzz rule to the input value.

    Args:
        inp (int): Input value.
        rule (tuple[int, str]): Rule to be applied.

    Returns:
        str: Response to be returned.
    """

    return rule[1] if inp % rule[0] == 0 else ""


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
