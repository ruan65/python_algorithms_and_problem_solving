from collections import deque


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
    lst = [9, 10, 9, 1, -7, -4, -8, 2, -6]

    print(Solution().maxSlidingWindow(lst, 4))
