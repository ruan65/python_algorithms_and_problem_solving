class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        cnv = x
        while cnv > 0:
            res += cnv % 10
            if cnv > 9:
                res *= 10
            cnv = cnv // 10
        return res == x

if __name__ == '__main__':
    print(Solution().isPalindrome(101))