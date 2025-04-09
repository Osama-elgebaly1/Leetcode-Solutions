# 1342. Number of Steps to Reduce a Number to Zero
# Problem: Given a number num, return the number of steps to reduce it to zero. 
# In one step, you can either subtract 1 from num or divide num by 2 (if num is even).

class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0  # Initialize a counter for steps
        while num > 0:  # Continue until num is reduced to 0
            if num % 2 == 0:  # If num is even, divide by 2
                num //= 2
            else:  # If num is odd, subtract 1
                num -= 1
            steps += 1  # Increment the step counter
        return steps  # Return the total number of steps
