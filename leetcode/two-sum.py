class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_seen = {}

        for ind, num in enumerate(nums):
            complement = target - num

            if complement in nums_seen:
                return [nums_seen[complement], ind]
            
            nums_seen[num] = ind

        return []