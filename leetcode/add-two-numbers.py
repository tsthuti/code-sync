# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        strl1=""
        strl2=""

        while l1:
            strl1 += str(l1.val)
            l1 = l1.next
        while l2:
            strl2 += str(l2.val)
            l2 = l2.next

        strl1 = strl1[::-1]
        strl2 = strl2[::-1]

        sum = int(strl1) + int(strl2)
        sum = str(sum)[::-1]
        sum = [int(c) for c in sum]
        
        head = ListNode()
        curr = head

        for c in sum[:-1]:
            curr.val = c
            curr.next = ListNode()
            curr = curr.next
        curr.val = sum[-1]
        
        return head