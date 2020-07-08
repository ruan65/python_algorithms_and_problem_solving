class Solution:
    def partitionLabels(self, S: str) -> [int]:
        if not S:
            return []
        i = 0
        end = 1
        while i < end:
            end = max(end, S.rfind(S[i], i + 1) + 1)
            i += 1

        return [i] + self.partitionLabels(S[i:])


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
