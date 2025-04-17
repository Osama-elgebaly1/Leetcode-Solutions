class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 🔍 Intuition:
        # Use a dictionary to store numbers and their indices as you iterate.
        # For each number, check if its complement (target - num) is already in the dict.

        indexes = {}  # Store number -> index
        for i, num in enumerate(nums):
            compliment = target - num  # Value needed to reach the target
            if compliment in indexes:  # If found, return the pair of indices
                return [indexes[compliment], i]
            indexes[num] = i  # Otherwise, store the current number and index
