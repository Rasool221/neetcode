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

        def safe_access(i: int, arr: list[int]) -> int:
            if i > len(arr) - 1:
                return 0
            
            return arr[i]

        l1_arr = get_arr(l1)
        l2_arr = get_arr(l2)

        ans: list[Optional[ListNode]] = []
        carry = 0
        max_len = max(len(l1_arr), len(l2_arr))
        for i in range(max_len):
            ij_sum = safe_access(i, l1_arr) + safe_access(i, l2_arr)

            if carry > 0:
                ij_sum += carry
                carry -= 1

            if ij_sum > 10:
                carry += 1
                ij_sum -= 10
            
            if len(ans) == 0:
                ans.append(ListNode(ij_sum))
            else:
                last_node = ans[len(ans)-1]
                new_node = ListNode(ij_sum)
                last_node.next = new_node
                ans.append(new_node)

        if carry > 0:
            last_node = ans[len(ans)-1]
            new_node = ListNode(1)
            last_node.next = new_node
            ans.append(new_node)
        
        return ans[0] if len(ans) > 0 else None