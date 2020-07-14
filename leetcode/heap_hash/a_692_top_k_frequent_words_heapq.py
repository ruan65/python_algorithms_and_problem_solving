import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, words: [str], k: int) -> [str]:

        dct = Counter(words)
        heap, result = [], []

        for key, val in dct.items():
            heapq.heappush(heap, (-val, key))

        while k:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result


if __name__ == '__main__':
    inp = ["the", "day", "is", "a", "sunny", "the", "the", "the", "sunny", "is", "is", "a", "a", "a", ]
    # to_dict = words_to_dict(inp)
    # print(to_dict)
    # rvrs = reverse_dict(to_dict)
    # print(rvrs)

    print(Solution().topKFrequent(inp, 4))
