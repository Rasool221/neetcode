# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        prev = None

        while l1 or l2:
            l1n = l1.val
            l2n = l2.val
            n = l1n + l2n

            if n > 9:
                prev_inner = prev
                head_inner = prev
                while n > 0:
                    k = n % 10
                    # print(k)
                    new = ListNode(k)

                    if not head_inner:
                        head_inner = new

                    if prev_inner:
                        prev_inner.next = new
                    
                    n //= 10
                    prev_inner = new

                result = head_inner
            else:
                result = ListNode(n)
        
            if new_head is None:
                new_head = result
            
            if prev:
                prev.next = result

            prev = result
            l1 = l1.next
            l2 = l2.next
            

        return new_head
