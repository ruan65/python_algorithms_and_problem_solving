# arr = [4, 5, 6, 7, 0, 1, 2]
# arr = [4]
# arr = [4, 5, 6, 7, 8, 70, 90, 0]
# arr = [4, 5, 6, 1, 2]
trgt = 0


def _find_pivot(arr: [int], s, e, m) -> int:
    if len(arr) == 1 or arr[0] < arr[len(arr) - 1]:
        return 0
    if arr[m] < arr[m - 1]:
        return m
    elif arr[m + 1] < arr[m]:
        return m + 1
    elif arr[m] > arr[0]:
        s = m + 1
    else:
        e = m
    return _find_pivot(arr, s, e, (s + e) // 2)


def find_pivot(arr: [int]) -> int:
    s = 0
    e = len(arr)
    m = (s + e) // 2
    return _find_pivot(arr, s, e, m)


def find_target_index(arr: [int], pivot: int, target: int) -> int:
    if target == arr[pivot]:
        return pivot
    if pivot == 0:
        return find_index(arr, target)
    elif target > arr[len(arr) - 1]:
        return find_index(arr[:pivot], target)
    else:
        indx = find_index(arr[pivot:], target)
        if indx != -1:
            indx += pivot
        return indx


def find_index(arr: [int], el: int) -> int:
    try:
        return arr.index(el)
    except ValueError:
        return -1


class Solution:
    def search(self, nums: [int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        pv = find_pivot(nums)
        return find_target_index(nums, pv, target)


if __name__ == '__main__':
    lst = [3, 1]
    pv = find_pivot(lst)
    print(pv)
    ind = find_target_index(lst, pv, 0)
    print(ind)
