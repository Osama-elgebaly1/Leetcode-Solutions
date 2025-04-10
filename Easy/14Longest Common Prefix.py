class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""  # Return empty if input list is empty

        prefix = strs[0]  # Assume first string is the prefix
        for s in strs[1:]:  # Iterate over the rest of the strings
            while not s.startswith(prefix):  # Reduce prefix until it's a prefix of s
                prefix = prefix[:-1]  # Trim the last character
                if not prefix: return ""  # If prefix becomes empty, return ""
        return prefix  # Return the longest common prefix
