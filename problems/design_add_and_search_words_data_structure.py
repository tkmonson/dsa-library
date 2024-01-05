'''
Design Add and Search Words Data Structure (#211)

Design a data structure that supports adding new words and determining if a
string matches any previously added string.

Implement the WordDictionary class:

    * WordDictionary(): Initializes the object.
    * add_word(word): Adds word to the data structure.
    * search(word): Returns true if there is a string in the data structure
      that matches word, false otherwise. word may contain dots (`.`), where a
      dot can match any letter.
'''

class KNode:
    def __init__(self, value):
        self.value = value
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.head = KNode(None)


    def add_word(self, word: str) -> None:
        curr = self.head
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = KNode(ch)
            curr = curr.children[ch]
        if None not in curr.children:
            curr.children[None] = KNode(None)


    def search(self, word: str) -> bool:
        def dfs(curr, i):
            if i == len(word):
                return None in curr.children

            if word[i] == '.':
                for ch in curr.children:
                    if dfs(curr.children[ch], i + 1):
                        return True
                return False

            if word[i] in curr.children:
                return dfs(curr.children[word[i]], i + 1)

            return False

        return dfs(self.head, 0)


if __name__ == '__main__':
    wd = WordDictionary()
    wd.add_word('bad')
    wd.add_word('dad')
    wd.add_word('mad')
    print(wd.search('pad'))
    print(wd.search('bad'))
    print(wd.search('.ad'))
    print(wd.search('.at'))
    print(wd.search('b..'))

'''
Dot can match any letter => search all paths below dot => backtracking =>
recursion => tree object. Nested dictionary representation is an elegant way to
implement a trie, but I don't think it would work well here, given the need to
traverse back up the tree.
'''

