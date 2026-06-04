# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        nums = []

        for curr in [list1, list2]:
            while curr:
                nums.append(curr.val)
                curr = curr.next
        
        if not nums:
            return None
            
        nums.sort()
        
        head = ListNode(nums[0])
        curr = head
        for val in nums[1:]:
            curr.next = ListNode(val)
            curr = curr.next
            
        return head