import numpy as np
import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # first find the element in the list
        if target in nums:
            return nums.index(target)
        else:
            return bisect.bisect_left(nums, target)