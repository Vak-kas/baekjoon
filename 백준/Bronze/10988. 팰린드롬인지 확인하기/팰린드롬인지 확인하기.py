import sys
a = sys.stdin.readline().rstrip()

if a == a[::-1]:
    print(1)
else:
    print(0)