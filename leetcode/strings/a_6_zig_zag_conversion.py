class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows < 2 or numRows >= len(s):
            return s

        arr = ['' for _ in range(numRows)]
        dw = True
        ind = 0
        for i in range(len(s)):
            arr[ind] += s[i]
            if ind == numRows - 1:
                dw = False
            if ind == 0:
                dw = True
            if dw:
                ind += 1
            else:
                ind -= 1
        return "".join(arr)
