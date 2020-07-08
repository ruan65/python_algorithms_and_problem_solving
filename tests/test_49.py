from leetcode.hash_tables.a_49_group_anagrams import group_anagrams


def test_find_pivot():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) is [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ]
