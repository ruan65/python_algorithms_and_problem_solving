def b_search_recur(numbers: [int], target: int) -> bool:
    if not numbers:
        return False
    m = len(numbers) // 2
    if target == numbers[m]:
        return True
    elif target > numbers[m]:
        return b_search_recur(numbers[m + 1:], target)
    else:
        return b_search_recur(numbers[:m], target)


def _b_search_recur_poi(numbers: [int], target: int, s: [int], e: [int]) -> bool:
    if s > e:
        return False

    else:
        m = s + (e - s) // 2
        if numbers[m] == target:
            return True
        elif target < numbers[m]:
            return _b_search_recur_poi(numbers, target, s, m - 1)
        else:
            return _b_search_recur_poi(numbers, target, m + 1, e)


def b_search_recur_poi(numbers: [int], target: int) -> bool:
    s = 0
    e = len(numbers) - 1
    return _b_search_recur_poi(numbers, target, s, e)


#     [1,2,3,4,5,77,898]
# def b_search_iterative(numbers: [int], target: int) -> bool:
#     s = 0
#     e = len(numbers) - 1
#     while s <= e:
#         m = s + (e - s) // 2
#         if numbers[m] == target:
#             return True
#         if target > numbers[m]:
#             s = m + 1
#         else:
#             e = m - 1
#     return False

def b_search_iterative(numbers: [int], target: int) -> bool:
    s = 0
    e = len(numbers)
    while s != e:
        m = s + (e - s) // 2
        if numbers[m] == target:
            return True
        if target > numbers[m]:
            s = m + 1
        else:
            e = m
    return False


if __name__ == '__main__':
    print(b_search_recur(numbers=[1, 2, 3], target=3))
    print(b_search_iterative(numbers=[1, 2, 3], target=3))
