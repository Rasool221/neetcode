class Solution:    
    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1

        # ensure head1 starts with the smaller value
        if head2.val < head1.val:
            head1, head2 = head2, head1

        og_head = head1
        head1prev = None

        while head1 and head2:
            if head1.val <= head2.val:
                head1prev = head1
                head1 = head1.next
            else:
                temp = head2.next
                head1prev.next = head2
                head2.next = head1

                head1prev = head2
                head2 = temp

        if head2:
            head1prev.next = head2

        return og_head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        head = lists[0]

        for l in lists[1:]:
            head = self.merge(head, l)

        return head