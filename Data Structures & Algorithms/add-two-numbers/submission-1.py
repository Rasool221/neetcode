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

        if len(l1_arr) != len(l2_arr):
            raise Exception("fuck")

        ans: list[Optional[ListNode]] = []
        carry = 0
        for i in range(len(l1_arr)):
            ij_sum = l1_arr[i] + l2_arr[i]

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