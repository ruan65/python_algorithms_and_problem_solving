def _recursive_binary_search(inp: [int], target: [int], start: [int], end: [int]) -> int:
    midpoint = start + (end - start) // 2
    if inp[midpoint] == target:
        return midpoint
    else:
        if target < inp[midpoint]:
            return _recursive_binary_search(inp, target, start, midpoint - 1)
        else:
            return _recursive_binary_search(inp, target, midpoint + 1, end)


def bs(inp: [int], target: [int]) -> bool:
    if not inp:
        return False
    if len(inp) == 1:
        return inp[0] == target
    mid = len(inp) // 2
    if target < inp[mid]:
        return bs(inp[:mid], target)
    else:
        return bs(inp[mid:], target)


if __name__ == '__main__':
    lst = [1, 2, 3]
    print(bs(lst, 3))
