# count = 0
#
#
# def get_all_permutations(word, res=[], step=0):
#     global count
#     count += 1
#     if step == len(word):
#         res.append("".join(word))
#
#     for i in range(step, len(word)):
#         string_copy = list(word)
#         string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
#         get_all_permutations(string_copy, res, step + 1)
#     return res

def get_all_permutations(txt: str) -> [str]:
    def bt(arr: [str], left: int, right: int):
        global count
        count += 1
        if left == right:
            res.append(''.join(arr))
        else:
            for i in range(left, right+1):
                arr[left], arr[i] = arr[i], arr[left]
                bt(arr, left + 1, right)
                arr[left], arr[i] = arr[i], arr[left]  # backtrack

    res = []
    bt(list(txt), 0, len(txt)-1)
    return res


if __name__ == '__main__':
    txt = 'abc'
    print(get_all_permutations(txt))
    print(count)
    print(2 ** len(txt))
