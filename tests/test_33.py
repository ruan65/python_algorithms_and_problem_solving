from leetcode.search.a_33_search_in_rotated_sorted_array import find_pivot, Solution


def test_find_pivot():
    assert find_pivot([4, 5, 6, 1, 2]) is 3
    assert find_pivot([4]) is 0
    assert find_pivot([4, 1]) is 1
    assert find_pivot([1, 2, 3]) is 0


def test_find_solution():
    assert Solution().search([4, 5, 6, 1, 2], 5) is 1
    assert Solution().search([4, 5, 6, 1, 2], 20) is -1
    assert Solution().search([5], 5) is 0
    assert Solution().search([], 5) is -1
    assert Solution().search([1, 3], 3) is 1
    assert Solution().search([3, 1], 3) is 0
    assert Solution().search([3, 1], 0) is -1
    assert Solution().search([5, 1, 3], 3) is 2
    assert Solution().search([50, 1, 3, 20, 21, 23], 21) is 4
