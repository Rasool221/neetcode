# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return

        # find mid point
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # slow: 3 -> 4 -> 5 -> 6
        # head: 0 -> 1 -> 2 -> 3

        # reverse second half
        # 3 -> 4 -> 5 -> 6
        # 3 <- 4 <- 5 <- 6
        cur = slow
        prev = None
        while cur:
            temp = cur.next
            if prev is None:
                cur.next = None
            else:
                cur.next = prev

            prev = cur
            cur = temp

        # head: 2 -> 4
        # prev: 10 -> 8 -> 6

        # prev is now head of reversed second half
        # now we merge first & second half
        one = head
        two = prev
        while one and two:
            # if one:
            #     print("one", one.val)
            # if two:
            #     print("two", two.val)
            one_temp = one.next
            two_temp = two.next

            one.next = two
            if one_temp:
                two.next = one_temp
            
            one = one_temp
            two = two_temp

        
            

