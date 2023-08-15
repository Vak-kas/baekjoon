import sys;

a, b = map(int, sys.stdin.readline().split());

c = a*b;

lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
    print(i-c, end=" ");