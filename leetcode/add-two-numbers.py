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

        # strategy: we will be looping over the values and adding them in the correct order, basically collapsing on top of the other
        l1_vals = []
        l2_vals = []

        l1_current = l1
        l2_current = l2

        while l1_current.next:
            l1_vals.append(l1_current.val)
            l1_current = l1_current.next
        l1_vals.append(l1_current.val)

        while l2_current.next:
            l2_vals.append(l2_current.val)
            l2_current = l2_current.next
        l2_vals.append(l2_current.val)

        l2_vals=l2_vals[::-1]
        l1_vals=l1_vals[::-1]
        
        l1_num = int("".join(str(num) for num in l1_vals))
        l2_num = int("".join(str(num) for num in l2_vals))

        sumnums = l1_num + l2_num
        reversed_num = str(sumnums)[::-1]

        final = ListNode()
        current = final
        for idx, char in enumerate(reversed_num):
            current.val = int(char)
            if idx == len(reversed_num)-1:
                current.next = None
            else:
                current.next = ListNode()
                current = current.next

        return final