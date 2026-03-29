# everything is standard, however the most difficult part 
# is to get the LRU item. if LRU item is popped, we also need the second most LRU item behind it, and so forth
# this is a "stack" like datastructure, except we need to do O(1) lookups, as well as know where the LRU item is
# hashmap for O(1) lookups in conjuction with some other DS that allows for ordering (to get LRU)
# hashmap with stack DS? cannot promote item to MRU in O(1) time with stack, but we can with linked list
# hashmap with linkedlist (doubly or singly)?
# map: key -> node 
# so we can promote items to MRU in O(1) time (end of list), and always know where LRU is (head of list)
# for capacity, we can do len(map) which is O(1)
# we need to keep track of the tail item in the LL, how do we do that?
# when we're inserting, we're always inserting at the end, so we can just keep track
# of last inserted (tail), and if its modified, we also update the tail


class Node:
    def __init__(self, val: int, key: int, prev: Optional[Node], next: Optional[Node]):
        self.val = val
        self.key = key

        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.head = None
        self.tail = None

        self.cap = capacity

    def make_mru(self, node: Node):
        # moving head
        if self.head == node and node.next:
            self.head = node.next
 
        # promote item to MRU
        if node.next and node.prev:
            node.prev.next = node.next
        elif node.next:
            node.next.prev = None

        # put at the end
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1

        node = self.hmap[key]
        self.make_mru(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if len(self.hmap) >= self.cap:
            del self.hmap[self.head.key]
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None

        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.make_mru(node)
        else:
            node = Node(value, key, self.tail, None)

            if self.tail:
                self.tail.next = node
            
            self.tail = node
            self.hmap[key] = node

            if self.head is None:
                self.head = node
                self.tail = node

        

