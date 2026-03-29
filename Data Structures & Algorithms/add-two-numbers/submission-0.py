# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_arr(node: Optional[ListNode]):
            if node is None:
                return []

            return [node.val] + get_arr(node.next)

        l1_arr = get_arr(l1)
        l2_arr = get_arr(l2)

        l1_int = int("".join(l1_arr[::-1]))
        l2_int = int("".join(l2_arr[::-1]))
    
        print(l1_int)
        print(l2_int)

        return []