# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        prev1 = prev2 = None
        new_head = None
        while cur1 is not None and cur2 is not None:
            cur1next = cur1.next
            cur2next = cur2.next
            
            if cur1.val <= cur2.val:
                cur1.next = cur2
                if prev2 is not None:
                    prev2.next = cur1
                if new_head is None:
                    new_head = cur1
            elif cur1.val > cur2.val:
                cur2.next = cur1
                if prev1 is not None:
                    prev1.next = cur2
                if new_head is None:
                    new_head = cur2
            
            prev1 = cur1
            prev2 = cur2
            cur1 = cur1next
            cur2 = cur2next

        if list1 and list2:
            return new_head
        
        return list1 if list2 is None else list2