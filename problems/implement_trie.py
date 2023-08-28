'''
Implement Trie (#208)

Implement a Trie data structure with `insert`, `search`, and `starts_with`
methods. `search` returns True if and only if the word was previously inserted
in the trie. `starts_with` returns True if there is a previously inserted word
in the trie that has the prefix `prefix`.
'''

# Left-child, right-sibling binary tree representation

class BNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BTrie:
    def __init__(self):
        self.head = None


    def insert(self, word: str) -> None:
        if not self.head:
            self.head = BNode(word[0])

        curr = self.head
        for i in range(len(word)):
            ch = word[i]
            while curr.right and curr.value != ch:
                curr = curr.right
            if curr.value != ch:
                curr.right = BNode(ch)
                curr = curr.right
            if not curr.left:
                curr.left = BNode(word[i + 1] if i + 1 < len(word) else None)
            curr = curr.left

        if curr.value:
            while curr.right:
                curr = curr.right
            curr.right = BNode(None)


    def _search(self, word: str) -> BNode | None:
        if not self.head:
            return None

        curr = self.head
        for ch in word:
            while curr and curr.value != ch:
                curr = curr.right
            if not curr:
                return None
            curr = curr.left

        return curr


    def search(self, word: str) -> bool:
        curr = self._search(word)
        while curr and curr.value:
            curr = curr.right
        return bool(curr)


    def starts_with(self, prefix: str) -> bool:
        return bool(self._search(prefix))


# K-ary tree representation

class KNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class KTrie:
    def __init__(self):
        self.head = KNode(None)


    def insert(self, word: str) -> None:
        curr = self.head
        for ch in word:
            ch_found = False
            for node in curr.children:
                if node.value == ch:
                    ch_found = True
                    curr = node
                    break
            if not ch_found:
                curr.children.append(KNode(ch))
                curr = curr.children[-1]

        end_found = False
        for node in curr.children:
            if not node.value:
                end_found = True
        if not end_found:
            curr.children.append(KNode(None))


    def _search(self, word: str) -> KNode | None:
        curr = self.head
        for ch in word:
            ch_found = False
            for node in curr.children:
                if node.value == ch:
                    ch_found = True
                    curr = node
                    break
            if not ch_found:
                return None
        return curr


    def search(self, word: str) -> bool:
        curr = self._search(word)
        if curr:
            for node in curr.children:
                if not node.value:
                    return True
        return False


    def starts_with(self, prefix: str) -> bool:
        return bool(self._search(prefix))


# Nested dictionary representation

class Trie:
    def __init__(self):
        self.trie = {}


    def insert(self, word: str) -> None:
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        t[None] = {}


    def _search(self, word: str) -> dict | None:
        t = self.trie
        for ch in word:
            if not ch in t:
                return None
            t = t[ch]
        return t


    def search(self, word: str) -> bool:
        t = self._search(word)
        return t and None in t


    def starts_with(self, prefix: str) -> bool:
        return bool(self._search(prefix))


if __name__ == '__main__':
    t = Trie()
    print("Insert 'apple'"); t.insert('apple')
    print(f"Search 'apple': {t.search('apple')}")
    print(f"Search 'app': {t.search('app')}")
    print(f"Starts with 'app': {t.starts_with('app')}")
    print("Insert 'app'"); t.insert('app')
    print(f"Search 'app': {t.search('app')}")

