import sys

print(sys.version_info)

l1 = list(range(1,1_000_000))
l2 = [1,2,3,4,5,6,7,8,9]

print(f'l1 size: {sys.getsizeof(l1)}')
print(f'l2 size: {sys.getsizeof(l2)}')