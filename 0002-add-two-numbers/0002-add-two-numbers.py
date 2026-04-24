# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2
        
        over = False
    
        first = None
        curr = None
        while curr1 or curr2:
            val1, val2 = 0, 0

            if curr1:
                val1 = curr1.val
                curr1 = curr1.next

            if curr2:
                val2 = curr2.val
                curr2 = curr2.next

            sum_v = val1 + val2

            if over:
                sum_v += 1
                over = False

            a = sum_v % 10
            b = sum_v // 10

            if b: over = True

            node = ListNode(a, None)

            if not first:
                first = node
                curr = node
            else:
                curr.next = node
                curr = node

        if over:
            curr.next = ListNode(1, None)

        return first
