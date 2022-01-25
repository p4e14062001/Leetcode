# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        size1 = 0
        size2 = 0
        d1 = l1
        d2 = l2
        while d1 or d2:
            if d1:
                size1 += 1
                d1 = d1.next
            if d2:
                size2 += 1
                d2 = d2.next
        n1 = l1
        n2 = l2
        if size1 < size2:
            n1 = l2
            n2 = l1
        carry = 0
        while n2:
            n1.val = n1.val + n2.val + carry
            carry = n1.val // 10
            n1.val = n1.val % 10
            n1 = n1.next
            n2 = n2.next
        while n1:
            n1.val = n1.val + carry
            carry = n1.val // 10
            n1.val = n1.val % 10
            n1 = n1.next
        if carry != 0:
            c = l1
            if size1 < size2:
                c = l2
            while c.next:
                c = c.next
            c.next = ListNode(carry)
        if size1 < size2:
            return l2
        return l1
