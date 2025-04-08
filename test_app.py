import pytest
from app import StringUtils

utils = StringUtils()

def test_palindromes():
    assert utils.isPalindrome("Madam") == True
    assert utils.isPalindrome("Radar") == True
    assert utils.isPalindrome("A") == True
    assert utils.isPalindrome("") == True

def test_non_palindromes():
    assert utils.isPalindrome("Hello") == False
    assert utils.isPalindrome("Python") == False

def test_none_input():
    assert utils.isPalindrome(None) == False