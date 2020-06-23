# f_reader = open('input__.txt', 'r')
#
# list_count = int(f_reader.readline())
#
# tracker = [0] * list_count
# sizes = [0] * list_count
#
# arr_map = {}
#
# result = []
#
# for i in range(list_count):
#     line = f_reader.readline().strip().split(' ')
#     ints = [int(i) for i in line]
#     sizes[i] = ints[0]
#     arr_map[i] = ints[1:]
#
#
# def append_min():
#     heads = []
#     for k, v in arr_map.items():
#         if tracker[k] < (sizes[k] - 1):
#             heads.append(v[0])
#             tracker[k] += 1
#
#     min_val = min(heads)
#     result.append(min_val)
#     pop_min(min_val)
#
#
# def pop_min(value):
#     for k, v in arr_map.items():
#         if len(v) > 0 and value == v[0]:
#             v.pop()
#
#
# print(arr_map)
# append_min()
# print(arr_map)
# print(result)
# f_reader.close()
