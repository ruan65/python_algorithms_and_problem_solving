def find_index(arr: [int], el: int) -> int:
    try:
        return arr.index(el)
    except ValueError:
        return -1
