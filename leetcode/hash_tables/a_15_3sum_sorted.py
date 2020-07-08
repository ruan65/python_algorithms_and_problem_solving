def find_3sum(arr: [int]) -> [[int]]:
    result: [[int]] = []
    if len(arr) < 3:
        return result
    if len(arr) == 3 and sum(arr) == 0:
        result.append(arr)
        return result
    if len(arr) > 2 and set(arr) == {0}:
        return [[0, 0, 0]]

    arr.sort()
    for i in range(len(arr) - 2):
        if i == 0 or (i > 0 and arr[i] != arr[i - 1]):
            low = i + 1
            high = len(arr) - 1
            sm = 0 - arr[i]

            while low < high:
                if sm == arr[low] + arr[high]:
                    result.append([arr[i], arr[low], arr[high]])
                    while arr[low] == arr[low + 1]:
                        low += 1
                        if low > len(arr) - 2:
                            break
                    while arr[high] == arr[high - 1]:
                        high -= 1
                        if high < 1:
                            break
                    low += 1
                    high -= 1
                elif arr[low] + arr[high] > sm:
                    high -= 1
                else:
                    low += 1

    return result


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        return find_3sum(nums)


if __name__ == '__main__':
    # data = [-1, 0, 1, 2, -1, -4]
    # data = [1, 1, -2]
    # data = [0, 0, 0]
    # data = [0, 0, 0, 0]
    # data = [-1, 0, 1]
    # data = [1, 2, -2, -1]
    # data = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    # data = [0, 4, 0, -2, 3, 1, -5, 0]
    # data = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    # data = [1, -1, -1, 0]
    data = [2, 0, -2, -5, -5, -3, 2, -4]
    print(find_3sum(data))
    # print(find_3sum(big_list))
