memo = [0, 1, 2, 4];


import sys;

t = int(sys.stdin.readline().rstrip());
for i in range(4, 12):
    value = memo[i-1] + memo[-2] + memo[-3];
    memo.append(value);
for _ in range(t):
    
    n = int(sys.stdin.readline().rstrip());
    print(memo[n])
