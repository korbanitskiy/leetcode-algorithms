"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Follow up: Could you solve it without converting the integer to a string?
"""

def palindrome(number):
    if number < 0:
        return False

    if number % 10 == 0 and number != 0:
        return False

    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number // 10

    for pos in range(len(digits) // 2):
        if digits[pos] != digits[-pos - 1]:
            return False

    return True


def palindrome_half_reversed(number):
    if number < 0:
        return False

    if number % 10 == 0 and number != 0:
        return False

    half_reverted = 0
    while number > half_reverted:
        half_reverted = half_reverted * 10 + number % 10
        number = number // 10

    return number == half_reverted or number == half_reverted // 10


def palindrome_str(number):
    return str(number) == str(number)[::-1]



if __name__ == "__main__":
    for fn in [palindrome, palindrome_half_reversed, palindrome_str]:
        assert fn(121) is True
        assert fn(10) is False
        assert fn(228899998822) is True
        assert fn(-345) is False
        assert fn(-121) is False
        assert fn(3344554432) is False
