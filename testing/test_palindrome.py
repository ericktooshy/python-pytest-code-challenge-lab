import pytest
from lib.palindrome import longest_palindromic_substring

def test_basic_palindrome():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_empty_string():
    assert longest_palindromic_substring("") == ""