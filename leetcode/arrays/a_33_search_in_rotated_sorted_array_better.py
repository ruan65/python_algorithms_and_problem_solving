def find_pivot(arr: [int]) -> int:
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return i
    return 0


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
