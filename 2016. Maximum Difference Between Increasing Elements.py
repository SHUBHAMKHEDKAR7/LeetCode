class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diif = -1
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    max_diif = max(max_diif , diff)
        return max_diif