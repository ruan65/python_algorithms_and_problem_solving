class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = 0
        self.prefixes = 0


def add(tree: TrieNode, word: str):
    cursor = tree
    for c in word:
        if not cursor.children.get(c):
            cursor.children[c] = TrieNode()
        cursor = cursor.children[c]
        cursor.prefixes += 1
    cursor.ends += 1


def count_prefixes(tree: TrieNode, pref: str) -> int:
    cursor = tree
    for c in pref:
        cursor = cursor.children.get(c)
        if not cursor:
            return 0
    return cursor.prefixes


if __name__ == '__main__':
    trie = TrieNode()
    add(trie, 'abba')
    add(trie, 'abbac')
    add(trie, 'abbacus')

    print(count_prefixes(trie, "abbac"))
