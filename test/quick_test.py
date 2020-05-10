from sort.quick import QuickSort
import datetime

a = list(range(500, 0, -1))
# a = [1, 3, 5, 2, 4, 1, 45, 1, 3, 5, 2, 4, 1, 45, -1, -3, -4, 1, 3, 5, 2, 4, 1, 45, 1, 3, 5, 2, 4, 1, 45, -1, -3, -4]
# a = [0]
c = datetime.datetime.now()
# print(c)
b = QuickSort.sort(a)
d = datetime.datetime.now()
print(d - c)
print(b)

