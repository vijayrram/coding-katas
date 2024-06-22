"""Test script for the FizzBuzz Kata version 2."""

import typing

import pytest
from fizzbuzz2 import fizzbuzz2


@pytest.mark.parametrize("number, result", [(1, "1"), (2, "2")])
def test_fizzbuzz2(number: int, result):
    """Test script to check the response of the fizzbuzz2 function.

    Args:
        number (int): Input number for the fizzbuzz2 function.
        result (str): The expected response from the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == result


@pytest.mark.parametrize("number", ["1", 1.0])
def test_fizzbuzz2_invalid_input_type(number: typing.Any):
    """Test script to check the response of the fizzbuzz2 function for invalid input types.

    Args:
        number (Any): Input for the fizzbuzz2 function.
    """

    with pytest.raises(TypeError, match=r"^Invalid input type.$"):
        fizzbuzz2(number)


@pytest.mark.parametrize("number", [6, 9])
def test_fizzbuzz2_div_by_3_only_but_not_containing_3_or_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers divisible by 3 only.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "Fizz"


@pytest.mark.parametrize("number", [10, 20])
def test_fizzbuzz2_div_by_5_only_but_not_containing_3_or_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers divisible by 5 only.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "Buzz"


@pytest.mark.parametrize("number", [60, 90])
def test_fizzbuzz2_div_by_15_but_not_containing_3_or_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers divisible by 15.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "FizzBuzz"


@pytest.mark.parametrize("number", [13, 23])
def test_fizzbuzz2_containing_3_and_not_5_but_not_divisible_by_3_or_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers divisible by 3 only.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "Fizz"


@pytest.mark.parametrize("number", [52, 56])
def test_fizzbuzz2_containing_5_and_not_3_but_not_divisible_by_3_or_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers divisible by 5 only.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "Buzz"


@pytest.mark.parametrize("number", [53])
def test_fizzbuzz2_containing_5_and_3_but_not_divisible_by_3_or_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers divisible by 3 and 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "FizzBuzz"


@pytest.mark.parametrize("number", [33, 36, 39])
def test_fizzbuzz2_containing_only_3_and_divisible_by_only_3(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "FizzFizz"


@pytest.mark.parametrize("number", [51, 54, 57])
def test_fizzbuzz2_containing_only_5_and_divisible_by_only_3(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "BuzzFizz"


@pytest.mark.parametrize("number", [513])
def test_fizzbuzz2_containing_3_and_5_and_divisible_by_only_3(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "FizzBuzzFizz"


@pytest.mark.parametrize("number", [130])
def test_fizzbuzz2_containing_only_3_and_divisible_by_only_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "FizzBuzz"


@pytest.mark.parametrize("number", [5, 25, 55])
def test_fizzbuzz2_containing_only_5_and_divisible_by_only_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "BuzzBuzz"


@pytest.mark.parametrize("number", [35])
def test_fizzbuzz2_containing_3_and_5_and_divisible_by_only_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "FizzBuzzBuzz"


@pytest.mark.parametrize("number", [30])
def test_fizzbuzz2_containing_only_3_and_divisible_by_3_and_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "FizzFizzBuzz"


@pytest.mark.parametrize("number", [45, 75])
def test_fizzbuzz2_containing_only_5_and_divisible_by_3_and_5(number: int):
    """Test script to check the response of the fizzbuzz2 function for numbers containing and
    divisible by 3 but not 5.

    Args:
        number (int): Input number for the fizzbuzz2 function.
    """

    response = fizzbuzz2(number)

    assert response == "BuzzFizzBuzz"
