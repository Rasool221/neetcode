# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        t = head
        h = head.next.next 

        while h is not None:
            if t == h:
                return True

            t = t.next

            if h.next:
                h = h.next.next 
            else:
                h = None
        
        return False