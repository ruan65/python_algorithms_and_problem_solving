# class Solution:
#     def search(self, nums: [int], tg: int) -> int:
#         def bs(lst: [int], st: int = 0) -> int:
#             if not lst:
#                 return -1
#             m = len(lst) // 2
#             if tg == lst[m]:
#                 return m + st
#             elif tg < lst[m]:
#                 return bs(lst[:m], st)
#             else:
#                 return bs(lst[m+1:], st + m + 1)
#         return bs(nums)


class Solution:
    def search(self, nums: [int], tg: int) -> int:
        s, e = 0, len(nums)
        while s != e:
            m = s + (e - s) // 2
            if tg == nums[m]:
                return m
            if tg < nums[m]:
                e = m
            else:
                s = m + 1
        return -1


# class Solution:
#     def search(self, nums: [int], target: int) -> int:
#         try:
#             return nums.index(target)
#         except:
#             return -1
