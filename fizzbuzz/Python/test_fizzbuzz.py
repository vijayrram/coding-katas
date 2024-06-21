"""Test script for the FizzBuzz Kata"""

import pytest

from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("inp, result", [(1, "1"), (2, "2")])
def test_fizzbuzz(inp: int, result):
    """Test script to check the response of the fizzbuzz function.

    Args:
        inp (int): Input number for the fizzbuzz function.
        result (str): The expected response from the fizzbuzz function.
    """

    response = fizzbuzz(inp)

    assert response == result
