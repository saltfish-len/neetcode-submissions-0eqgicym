class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.length = 0
        self.start = Node(None, None)
        self.end = Node(None, None)
        self.start.next = self.end
        self.end.prev = self.start
        self.cache = {} # key:[val, node]

    def get(self, key: int) -> int:
        if key in self.cache:
            # move it to end
            val, node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.end.prev.next = node
            node.prev = self.end.prev
            self.end.prev = node
            node.next = self.end
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            cur = Node(key,value)
            self.end.prev.next = cur
            cur.prev = self.end.prev
            cur.next = self.end
            self.end.prev = cur
            self.length += 1
            while self.length > self.cap:
                drop = self.start.next
                self.start.next = drop.next
                self.start.next.prev = self.start
                del self.cache[drop.key]
                del drop
                self.length -= 1
            self.cache[key] = [value, cur]
        if key in self.cache:
            val, node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.end.prev.next = node
            node.prev = self.end.prev
            self.end.prev = node
            node.next = self.end
            self.cache[key] = [value, node]
            
