def square_nums(nums):
    for n in nums:
        yield n*n

# sn = square_nums([2,3,4])
sn = iter([2,3,4])

print(next(sn))
print(next(sn))
print(next(sn))
print(next(sn, 10500))