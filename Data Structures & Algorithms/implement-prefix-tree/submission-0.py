class Node:
    def __init__(self):
        self.children = {}
        self.isend = False
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                cur.children[ch] = Node()
                cur = cur.children[ch]
        cur.isend = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        return cur.isend


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return False
        return True
        