def quick(lst: [int]) -> [int]:
    def sort(head: int, tail: int):
        if head >= tail:
            return
        s, e = head, tail
        mid = s + (e - s) // 2
        pvt = lst[mid]
        while s <= e:
            while s <= e and lst[s] < pvt:
                s += 1
            while s <= e and lst[e] > pvt:
                e -= 1
            if s <= e:
                lst[s], lst[e] = lst[e], lst[s]
                s += 1
                e -= 1
        sort(head, e)
        sort(s, tail)

    sort(0, len(lst) - 1)


class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        quick(nums)
        return nums
