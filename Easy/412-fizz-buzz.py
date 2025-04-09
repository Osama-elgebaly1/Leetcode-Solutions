# 412. Fizz Buzz
# Problem: Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three, output "Fizz" instead of the number, 
# and for the multiples of five, output "Buzz".
# For numbers which are multiples of both three and five, output "FizzBuzz".

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []  # Initialize an empty list to store results
        for i in range(1, n + 1):  # Iterate through numbers from 1 to n
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")  # If divisible by both 3 and 5
            elif i % 3 == 0:
                result.append("Fizz")  # If divisible by 3
            elif i % 5 == 0:
                result.append("Buzz")  # If divisible by 5
            else:
                result.append(str(i))  # Otherwise, append the number itself
        return result  # Return the result list
