# Given a list of words and a prefix, output the list of words from the input list that start with that prefix.

class TrieNode:

    def __init__(self, data):
        self.data = data
        self.end_word = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")
    
    def add(self, word):
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]

        curr.end_word = True

    def autocomplete(self, prefix):
        result = []
        prefix_end_node = self._get_prefix_end_node(prefix)

        if prefix_end_node is not None:
            self._dfs(prefix, prefix_end_node, result)

        return result

    def _get_prefix_end_node(self, prefix):
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return None
            curr = curr.children[letter]

        return curr

    def _dfs(self, prefix, curr, result):
        if curr.end_word:
            result.append(prefix)

        for child in curr.children.values():
            self._dfs(prefix + child.data, child, result)

if __name__ == "__main__":

    vocabulary = ["car", "camp", "catheter", "cart", "crab",
                  "cat", "apple", "ball", "boy", "bolster"]
    prefix = "ca"
    trie = Trie()
    
    for word in vocabulary:
        trie.add(word)

    print(trie.autocomplete(prefix))


# Note: the Trie class would ideally have remove and contain methods for completion, but they are not necessary for autocomplete.
