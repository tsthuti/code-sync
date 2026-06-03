class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for ind, num in enumerate(nums):
            compl = target - num
            if compl in hashmap:
                return [hashmap[compl], ind]
            else:
                hashmap[num] = ind

        return []