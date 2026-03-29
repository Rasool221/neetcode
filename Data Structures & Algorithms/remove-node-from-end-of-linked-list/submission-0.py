# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# an o(n) time and o(n) space is trivial, just store the 
# node ref and its location from the beginning

# in o(n) time but o(1) space, we cannot do that 
# a solution would be a 2 pass approach:
# - first pass: count the amount of nodes
# - second pass: using the above count, you can identify which node to remove 

# a 2 pass approach is o(n) time and o(1) space, but it 
# its 2 passes and im guessing we want a single pass approach

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        amt = 0
        cur = head
        while cur:
            amt += 1
            cur = cur.next

        i = 0
        i_d = amt - n # index to remove
        cur = head
        prev = None
        while cur:
            if i == i_d:
                if prev is None:
                    return None
                prev.next = cur.next
                break
            
            i += 1
            prev = cur
            cur = cur.next

        return head