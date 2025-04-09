# 9. Palindrome Number
# Problem: Given an integer x, return true if x is a palindrome, and false otherwise.
# An integer is a palindrome if it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # --------- Integer-Based Solution -------#
        original = x  # Store the original number to compare later
        converted = 0  # This will hold the reversed number
        while x > 0:  # While there are digits left in the original number
            last_digit = x % 10  # Get the last digit of the number
            converted = converted * 10 + last_digit  # Build the reversed number
            x = x // 10  # Remove the last digit from the original number
        return original == converted  # Compare the reversed number with the original number

        # ------------ Str Conversion --------------#

        # x = str(x)  # Convert the integer to a string
        # y = x[::-1]  # Reverse the string
        # if y == x:  # Check if the reversed string equals the original string
        #     return True
        # return False  # Return False if not a palindrome

