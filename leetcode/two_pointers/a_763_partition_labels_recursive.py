class Solution:
    def partitionLabels(self, S: str) -> [int]:
        if len(S) == 1:
            return [1]

        result: [int] = []

        last_indices: {str: int} = {letter: S.rindex(letter) for letter in S}

        for i in range(len(S)):
            last_indices[ord(S[i]) - ord('a')] = i

        start = 0
        end = 0
        for i in range(len(S)):
            end = max(end, last_indices[S[i]])
            if i == end:
                result.append(end - start + 1)
                start = end + 1

        return result


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
