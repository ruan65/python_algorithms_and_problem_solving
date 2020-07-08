class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        answer = cur = 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                answer = max(answer, cur)
                cur = 0
        return max(answer, cur)


if __name__ == '__main__':
    input = [1, 1, 0, 0]

    print(Solution().findMaxConsecutiveOnes(input))
