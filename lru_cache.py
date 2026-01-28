from node import Node


class LRUCache:
    """
    Least Recently Used (LRU) Cache Implementation
    """

    def __init__(self, capacity: int):

        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # ---------------- Internal Helpers ----------------

    def _remove(self, node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):

        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

    # ---------------- Public API ----------------

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to front (most recent)
        self._remove(node)
        self._add_to_front(node)

        return node.value

    def put(self, key, value):

        # If key exists
        if key in self.cache:

            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._add_to_front(node)

        else:

            # Evict if full
            if len(self.cache) == self.capacity:

                lru = self.tail.prev

                self._remove(lru)
                del self.cache[lru.key]

            node = Node(key, value)

            self.cache[key] = node
            self._add_to_front(node)

    def display(self):

        curr = self.head.next
        result = []

        while curr != self.tail:

            result.append(f"{curr.key}:{curr.value}")
            curr = curr.next

        return " -> ".join(result)
