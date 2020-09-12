class TrieNode:
    def __init__(self, data=None):
        self.pointers = [None for _ in range(26)]
        self.ends = 0
        self.starts = 0
        self.data = data


def char_index(ch: str) -> int:
    return ord(ch) - ord('a')


def is_last(i, w):
    return i == len(w) - 1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for i, c in enumerate(word):
            ind = char_index(c)
            nxt = curr.pointers[ind]
            if nxt:
                nxt.starts += 1
                if is_last(i, word):
                    nxt.ends += 1
                    return
                curr = nxt
            else:
                nxt = TrieNode(data=c)
                nxt.starts = 1
                if is_last(i, word):
                    nxt.ends += 1
                curr.pointers[ind] = nxt
                curr = nxt

    def search(self, word: str) -> (bool, int):
        curr = self.root
        for i, c in enumerate(word):
            nxt = curr.pointers[char_index(c)]
            if nxt:
                if is_last(i, word) and nxt.ends > 0:
                    return True, nxt.starts
                curr = nxt
            else:
                return False, 0
        return False, 0

    def count_prefix(self, pr: str) -> (bool, int):
        curr = self.root
        for i, c in enumerate(pr):
            nxt = curr.pointers[char_index(c)]
            if nxt:
                if is_last(i, pr):
                    return True, nxt.starts
                curr = nxt
            else:
                return False, 0
        return False, 0


if __name__ == '__main__':
    trie = Trie()
    # trie.add('eouecvksgllpvfxfvndu')
    # trie.add('uugxgcrtujxzyjysqrhu')
    trie.add('ryhlozedmgzcmjdfjhte')
    # trie.add('ibfzenldsdltkjbbsccq')
    # trie.add('vvxwlttswneoosvgfezt')
    # trie.add('qimoqjtjypqupwwrueew')
    # trie.add('nkaetboylnjbxxvhzupk')
    # trie.add('rdzddgjryupsyhhbjtmx')
    # trie.add('kudnlccqbvkizsfdbwxy')
    # trie.add('jgahjespbkxxeqnzwpjr')

    print(trie.count_prefix("yyr"))
