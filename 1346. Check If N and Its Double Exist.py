class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()

        for x in arr:
            if x * 2 in seen:
                return True
            if x % 2 == 0 and x // 2 in seen :
                return True
            seen.add(x)
        return False