class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ""
        for ch in s :
            if ch.isalnum() :
                new_s += ch.lower()
        return new_s == new_s[::-1]