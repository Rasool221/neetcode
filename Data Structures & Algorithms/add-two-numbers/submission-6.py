# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getListN(l: Optional[ListNode]) -> int:
            n = 0
            c = 0
            while l:
                n = l.val * 10**c + n
                l = l.next
                c += 1
            return n
        
        l1n = getListN(l1)
        l2n = getListN(l2)

        n = l1n + l2n

        print(l1n, l2n, n)

        if n == 0:
            return ListNode(0)

        head = None
        prev = None
        while n > 0:
            k = n % 10

            node = ListNode(k)

            if head is None:
                head = node

            if prev:
                prev.next = node

            prev = node

            n //= 10
        
        return head

