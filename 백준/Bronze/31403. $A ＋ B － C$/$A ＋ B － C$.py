import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

d = str(a) + str(b)
d = int(d) - c

print(a + b - c)
print(d)