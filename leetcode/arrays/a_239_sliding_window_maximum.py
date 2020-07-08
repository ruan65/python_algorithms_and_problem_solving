# class Solution:
#     def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
#         res = []
#         for i in range(len(nums) - k + 1):
#             res.append(max(nums[i:i + k]))
#         return res

from collections import deque


# class Solution:
#     def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
#         if not nums:
#             return []
#         res = []
#         dq = deque()
#         for i in range(k):
#             while dq:
#                 if nums[i] > nums[dq[-1]]:
#                     dq.pop()
#                 else:
#                     break
#
#             dq.append(i)
#         print(dq)
#         for i in range(k, len(nums)):
#             res.append(nums[dq[0]])
#             if dq[0] < i - k + 1:
#                 dq.popleft()
#             while dq:
#                 if nums[i] > nums[dq[-1]]:
#                     dq.pop()
#                 else:
#                     break
#             dq.append(i)
#             print(dq)
#         res.append(nums[dq[0]])
#         return res

class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        dq = deque()
        res = []
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


if __name__ == '__main__':
    lst = [9, 10, 9, -7, -4, -8, 2, -6]

    print(Solution().maxSlidingWindow(lst, 5))
