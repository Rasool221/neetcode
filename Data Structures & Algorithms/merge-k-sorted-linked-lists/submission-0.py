# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# pick the first linked list as the base, then combine with every other list, should be o(n*m)

class Solution:    
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        og_head = head1

        while head1 or head2:
            head1next = head1.next
            head2next = head2.next

            n1 = head1.val
            n2 = head2.val

            if n2 > n1:
                if head1.next and head1.next.val < n2:
                    head1 = head1.next
                    continue
                
                temp = head1.next
                head1.next = head2
                head2.next = temp
            elif n2 == n1:
                temp = head1.next
                head1.next = head2
                head2.next = temp

            head1 = head1next
            head2 = head2next

        return og_head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        head = lists[0]
        for h in lists[1:]:
            head = self.merge(head, h) 

        return head