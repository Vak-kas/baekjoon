import sys
up, down, height = map(int, sys.stdin.readline().split())

total = height - up

count = 1

a = total // (up-down)
b = total % (up-down)
# print(a, b)
if b > 0:
    count+=1



print(count + a)