# 1480. Running Sum of 1d Array
# Problem: Given an array nums, return an array such that each element at index i 
# is the sum of all the elements from index 0 to i (inclusive).
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []  # List to store running sum results
        total = 0  # Variable to track the cumulative sum
        
        for num in nums:  # Iterate through the input list
            total += num  # Add current number to the cumulative sum
            results.append(total)  # Append the current cumulative sum to the results
        
        return results  # Return the final list of running sums
