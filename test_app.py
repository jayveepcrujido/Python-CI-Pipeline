from app import StringUtils  # Removed unused 'pytest'

utils = StringUtils()


def test_palindromes():
    assert utils.isPalindrome("Madam")
    assert utils.isPalindrome("Radar")
    assert utils.isPalindrome("A")
    assert utils.isPalindrome("")


def test_non_palindromes():
    assert not utils.isPalindrome("Hello")
    assert not utils.isPalindrome("Python")


def test_none_input():
    assert not utils.isPalindrome(None)
