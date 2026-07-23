class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new = nums1 + nums2
        new.sort()
        n = len(new)
        mid = n // 2
        
        if n % 2 != 0:
            return new[mid]

        return (new[mid] + new[mid-1]) / 2.0