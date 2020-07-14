from collections import Counter


class Solution:
    def characterReplacement(self, txt: str, k: int) -> int:
        if not txt:
            return 0

        s = mx = 0
        count = Counter()

        for e in range(len(txt)):
            count[txt[e]] += 1
            if e - s + 1 - count.most_common(1)[0][1] > k:
                count[txt[s]] -= 1
                s += 1
            mx = max(mx, e - s + 1)
        return mx


if __name__ == '__main__':
    tx = 'ANNAZZZ'
    print(Solution().characterReplacement(tx, 2))
