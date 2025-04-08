class StringUtils:
    def isPalindrome(self, input_str):
        if input_str is None:
            return False
        reversed_str = input_str[::-1]
        return input_str.lower() == reversed_str.lower()  