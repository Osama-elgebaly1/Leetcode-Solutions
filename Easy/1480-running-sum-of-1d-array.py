# 1480. Running Sum of 1d Array
# Problem: Given an array nums, return an array such that each element at index i 
# is the sum of all the elements from index 0 to i (inclusive).

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Iterate through the list starting from index 1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]  # Add the previous element to the current one
        
        return nums  # Return the updated list

s1 = Solution()
print(s1.runningSum([1,2,3]))