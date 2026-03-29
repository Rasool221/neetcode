# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 -> 1 -> 2 -> 3
# 0 <- 1 <- 2 <- 3 = [3,2,1,0]
# keep a record of prev, and reverse arrows. 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur is not None:
            next_item = cur.next

            # reverse the refs
            if prev is not None:
                cur.next = prev
            else:
                cur.next = None
            
            prev = cur
            cur = next_item

        return prev