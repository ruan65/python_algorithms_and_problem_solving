class Solution:
    def canPartitionKSubsets(self, nums: [int], k: int) -> bool:
        size = len(nums)
        basket = [0 for _ in range(size)]
        amount = sum(nums) // k
        nums.sort(reverse=True)

        def track(i):
            if i == size:
                return True
            for b in range(k):
                basket[b] += nums[i]
                if basket[b] <= amount and track(i + 1):
                    return True
                basket[b] -= nums[i]  # backtrack
                if basket[b] == 0:
                    break
            return False

        return track(0)


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3))
