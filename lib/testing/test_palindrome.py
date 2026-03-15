import pytest
from lib.palindrome import longest_palindromic_substring

# Basic Functionality Tests

def test_babad(): 
    result = longest_palindromic_substring("babad")
    assert result in ["aba", "bab"]  # Both "aba" and "bab"

def test_cbbd():
    result = longest_palindromic_substring("cbbd")
    assert result == "bb"

def test_racecar():
    assert longest_palindromic_substring("racecar") == "racecar"

# Edge Case Testing 

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_characters_non_palindrome():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]  # Both "a" and "c"

def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"

def test_long_palindrome_inside():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

# Additional Edge Cases 

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_numeric_string():
    assert longest_palindromic_substring("12321") == "12321"

def test_mixed_letters_numbers():
    assert longest_palindromic_substring("a1b2b1a") == "a1b2b1a"


@pytest.mark.parametrize("value", [None, 123])
def test_non_string_input_raises_typeerror(value):
    with pytest.raises(TypeError):
        longest_palindromic_substring(value)


def test_no_palindrome_longer_than_one_character():
    s = "abcd"
    result = longest_palindromic_substring(s)
    assert len(result) == 1
    assert result in set(s)


def test_very_long_input_all_same_character():
    s = "a" * 1000
    assert longest_palindromic_substring(s) == s
