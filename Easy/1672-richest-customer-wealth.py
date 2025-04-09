# 1672. Richest Customer Wealth
# Problem: You are given a 2D array where each row represents a customer and each column 
# represents the balance of an account. Return the maximum wealth among all customers.

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Optimized approach: Using max() and sum() to get the maximum wealth
        return max(sum(account) for account in accounts)  # Find the maximum sum of each account's wealth

        ########## ----- Manual one -----------########
        # max_wealth = 0  # Initialize max wealth to 0
        # for ls in accounts:  # Iterate over each account list
        #     current = 0  # Track current wealth of an account
        #     for element in ls:  # Iterate over elements in the account
        #         current += element  # Add the element to current wealth
        #     if current > max_wealth:  # Check if current wealth is greater than max wealth
        #         max_wealth = current  # Update max wealth if needed
        # return max_wealth  # Return the max wealth found
