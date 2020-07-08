def get_all_permutations(txt: str) -> [str]:
    def bt(arr: [str], left: int, right: int):
        if left == right:
            res.append(''.join(arr))
        else:
            for i in range(left, right + 1):
                arr[left], arr[i] = arr[i], arr[left]
                bt(arr, left + 1, right)
                arr[left], arr[i] = arr[i], arr[left]  # backtrack

    res = []
    bt(list(txt), 0, len(txt) - 1)
    return res


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if len(tiles) == 1:
            return 1
        all_substrings = [""]
        perms = set()
        for ch in tiles:
            all_substrings += [s + ch for s in all_substrings]
        all_substrings.pop(0)
        for seq in all_substrings:
            perms.update(get_all_permutations(seq))
        return len(perms)
