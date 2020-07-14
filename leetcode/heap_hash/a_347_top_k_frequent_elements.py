import heapq
from collections import defaultdict


def top_k_frequent(arr: [int], h: int) -> [int]:
    dct = defaultdict(int)

    for i in arr:
        dct[i] += 1

    answer, heap = [], []

    for k, v in dct.items():
        heapq.heappush(heap, (-v, k))

    while h:
        heappop = heapq.heappop(heap)
        answer.append(heappop[1])
        h -= 1

    return answer


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        return top_k_frequent(nums, k)


if __name__ == '__main__':
    inp = [1, 1, 1, 7, 2, 3, 3, 4]
    print(top_k_frequent(inp, 4))
