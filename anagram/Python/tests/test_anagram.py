"""Test script for the Anagram kata."""

import pytest

from anagram import is_valid_two_word_anagram


@pytest.mark.parametrize(
    "string, words, result",
    [("saint", ["ant", "is"], True)],
    [("saint", ["ants", "i"], True)],
    [("saint", ["ants", "sit"], False)],
)
def test_is_valid_two_word_anagram(
    string: str,
    words: list[str],
    expected_result: bool,
) -> None:
    """Test to check if the given words are indeed an anagram.

    Args:
        string (str): String to be tested again.
        words (list[str]): Duo of words that should be checked.
        expected_result (bool): Result expected.
    """

    result = is_valid_two_word_anagram(string, words)

    assert result == expected_result


@pytest.mark.parametrize(
    "string, words, result",
    [("saint", ["an", "ant", "is"], True)],
)
def test_is_valid_two_word_anagram_not_two_words(
    string: str,
    words: list[str],
) -> None:
    """Test to check if the input words are exactly two in number.

    Args:
        string (str): String to be tested again.
        words (list[str]): Duo of words that should be checked.
    """

    with pytest.raises(ValueError, match="^Incorrect number of words.$"):
        is_valid_two_word_anagram(string, words)
