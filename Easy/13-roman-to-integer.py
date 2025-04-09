class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanian = {  # Mapping Roman numerals to their integer values
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0  # Initialize result to 0
        for i in range(len(s)):  # Loop through each character in the Roman numeral string
            if i + 1 < len(s) and romanian[s[i]] < romanian[s[i + 1]]:  # If current numeral is smaller than next
                result -= romanian[s[i]]  # Subtract current numeral's value
            else:
                result += romanian[s[i]]  # Otherwise, add current numeral's value
        
        return result  # Return the final integer result
