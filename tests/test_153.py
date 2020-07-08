from leetcode.search.a_153_find_min_in_rotated_sorted_arr import find_pivot, Solution


def test_find_pivot():
    assert find_pivot([4, 5, 6, 1, 2]) is 3
    assert find_pivot([4]) is 0
    assert find_pivot([4, 1]) is 1
    assert find_pivot([1, 2, 3]) is 0
    assert find_pivot([2, 3, 4, 5, 1]) is 4
    assert find_pivot([5, 1, 2, 3, 4]) is 1


def test_find_min():
    assert Solution().findMin([3, 4, 5, 1, 2]) is 1
    assert Solution().findMin([3, 4, 5, 0, 1, 2]) is 0
    assert Solution().findMin([3, 4, 5]) is 3
    assert Solution().findMin([3]) is 3
