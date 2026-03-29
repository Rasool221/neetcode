# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 1
        left = head
        new_head = None
        last_tail = None

        while head:
            head_next = head.next
            if c > 0 and c % k == 0:
                if last_tail:
                    last_tail.next = head

                if new_head is None:
                    new_head = head

                next_left = head.next

                cc = 0
                left_prev = None
                while left and cc < k:
                    if cc == 0:
                        last_tail = left

                    left_next = left.next 

                    if left_prev:
                        if left_prev.next == left:
                            left_prev.next = next_left 

                        left.next = left_prev

                    left_prev = left
                    left = left_next
                    cc += 1

                left = next_left

            c += 1
            head = head_next


        return new_head