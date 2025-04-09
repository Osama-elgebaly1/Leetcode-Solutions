# 9. Palindrome Number
# Problem: Given an integer x, return true if x is a palindrome, and false otherwise.
# An integer is a palindrome if it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:  # Negative numbers cannot be palindromes
            return False
        original = x  # Store the original number
        reversed_num = 0  # Initialize variable for reversed number
        
        while x > 0:  # Reverse the number
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return original == reversed_num  # Return True if the original number is equal to the reversed number
