from collections import namedtuple

rows = int(input())
Student = namedtuple('Student', input())
total = 0

for _ in range(rows):
    f1, f2, f3, f4 = input().split()
    st = Student(f1, f2, f3, f4)
    total += int(st.MARKS)
print(total / rows)
