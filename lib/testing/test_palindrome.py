from lib.palindrome import longest_palindromic_substring


def test_basic_palindrome():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]


def test_even_length_palindrome():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_no_palindrome():
    assert longest_palindromic_substring("abc") in ["a", "b", "c"]


def test_entire_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_repeated_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_long_palindrome():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"


def test_two_characters_same():
    assert longest_palindromic_substring("aa") == "aa"


def test_two_characters_different():
    assert longest_palindromic_substring("ab") in ["a", "b"]