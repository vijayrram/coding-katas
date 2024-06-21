"""Test script for the FizzBuzz Kata"""

import typing
import pytest

from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("number, result", [(1, "1"), (2, "2")])
def test_fizzbuzz(number: int, result):
    """Test script to check the response of the fizzbuzz function.

    Args:
        number (int): Input number for the fizzbuzz function.
        result (str): The expected response from the fizzbuzz function.
    """

    response = fizzbuzz(number)

    assert response == result


@pytest.mark.parametrize("number", ["1", 1.0])
def test_fizzbuzz_invalid_input_type(number: typing.Any):
    """Test script to check the response of the fizzbuzz function for invalid input types.

    Args:
        number (Any): Input for the fizzbuzz function.
    """

    with pytest.raises(TypeError, match=r"^Invalid input type.$"):
        fizzbuzz(number)


@pytest.mark.parametrize("number", [3, 6, 9])
def test_fizzbuzz_div_by_3_only(number: int):
    """Test script to check the response of the fizzbuzz function for numbers divisible by 3 only.

    Args:
        number (int): Input number for the fizzbuzz function.
    """

    response = fizzbuzz(number)

    assert response == "Fizz"


@pytest.mark.parametrize("number", [5, 10, 20])
def test_fizzbuzz_div_by_5_only(number: int):
    """Test script to check the response of the fizzbuzz function for numbers divisible by 5 only.

    Args:
        number (int): Input number for the fizzbuzz function.
    """

    response = fizzbuzz(number)

    assert response == "Buzz"


@pytest.mark.parametrize("number", [15, 30, 45])
def test_fizzbuzz_div_by_15(number: int):
    """Test script to check the response of the fizzbuzz function for numbers divisible by 15.

    Args:
        number (int): Input number for the fizzbuzz function.
    """

    response = fizzbuzz(number)

    assert response == "FizzBuzz"
