def heap_sort(lst: [int]):
    def heapify(n: int, i: int):
        l = 2 * i + 1
        r = l + 1
        mx = i
        if l < n and lst[mx] < lst[l]:
            mx = l
        if r < n and lst[mx] < lst[r]:
            mx = r
        if mx != i:
            lst[i], lst[mx] = lst[mx], lst[i]
            heapify(n, mx)

    for j in range(len(lst) // 2 + 1)[::-1]:
        heapify(len(lst), j)
    for k in range(len(lst))[::-1]:
        lst[0], lst[k] = lst[k], lst[0]
        heapify(k, 0)


class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        heap_sort(nums)
        return nums


if __name__ == '__main__':
    arr = [2, 5, 6, 7, 7754, 322, 444, 555, -100]
    Solution().sortArray(arr)
    print(arr)
