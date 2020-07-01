from collections import Counter


def words_to_dict(words: [str]) -> {str: int}:
    res: {str: int} = dict()
    for w in words:
        if w in res:
            res[w] += 1
        else:
            res[w] = 1
    return res


def reverse_dict(dct: {str: int}) -> {int: [str]}:
    res: {int: [str]} = dict()
    for k, v in dct.items():
        if v in res:
            arr = res[v]
            arr.append(k)
            arr.sort()
            res[v] = arr
        else:
            res[v] = [k]

    return res


def top_k_frequent(wrds: {int: [str]}, k: int) -> [str]:
    res = []
    frq = list(wrds.keys())
    frq.sort(reverse=True)

    for i in range(k):
        if i < len(frq):
            res.extend(wrds[frq[i]])
    return res[:k]


class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        # to_dict = words_to_dict(words)
        # rvrs = reverse_dict(to_dict)
        # return top_k_frequent(rvrs, k)
        return [ke for ke, v in sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))][:k]


if __name__ == '__main__':
    inp = ["the", "day", "is", "a", "sunny", "the", "the", "the", "sunny", "is", "is", "a", "a", "a", ]
    # to_dict = words_to_dict(inp)
    # print(to_dict)
    # rvrs = reverse_dict(to_dict)
    # print(rvrs)

    print(Solution().topKFrequent(inp, 4))
