# 1672. Richest Customer Wealth
# Problem: You are given a 2D array where each row represents a customer and each column 
# represents the balance of an account. Return the maximum wealth among all customers.

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0  # Initialize the variable to track the maximum wealth
        for account in accounts:  # Iterate through each customer's account balances
            max_wealth = max(max_wealth, sum(account))  # Find the max wealth by summing each account's balance
        return max_wealth  # Return the maximum wealth
