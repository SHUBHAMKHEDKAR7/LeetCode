"""
File : 520 Detect Capital.py
DATE : 2026-08-15
Day : Tuesday
author : Shubham Khedkar
 
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() :
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower() :
            return True
        else :
            return False