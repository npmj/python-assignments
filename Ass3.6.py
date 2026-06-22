import sys

data = int(input("Enter a value: "))

print(type(data))
print(id(data))

size = sys.getsizeof(data)
print(size)
