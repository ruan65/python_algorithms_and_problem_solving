from ya.split_num_array_into_ints import get_str_of_intervals


def test_get_str_of_intervals():
    assert get_str_of_intervals([]) == ''
    assert get_str_of_intervals([0]) == '0'
    assert get_str_of_intervals([1, 2, 3]) == '1-3'
