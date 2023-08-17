import sys
n = int(sys.stdin.readline().rstrip());

for i in range(1, n+1):
    tmp = sys.stdin.readline().rstrip();
    print(f"{i}. {tmp}")