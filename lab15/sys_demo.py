import sys

# print(sys.version_info)
# print(sys.executable)

# for el in sys.path:
# 	print(el)

l1 = range(1,5_000_000)
l2 = [1,2,3,4,5,6,7,8,9]

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))