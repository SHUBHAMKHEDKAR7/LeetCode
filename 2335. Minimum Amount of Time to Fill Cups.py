class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        total = sum(amount)
        maximum = max(amount)

        return max(maximum, (total + 1) // 2)

