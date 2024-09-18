import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a = int(sys.stdin.readline().rstrip())

    if a %2 == 0:
        print("even")
    else:
        print("odd")