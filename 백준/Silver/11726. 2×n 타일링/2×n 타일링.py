import sys;

n = int(sys.stdin.readline().rstrip());
memo = [0, 1, 2];

if n<2:
    print(memo[n]);
else:
    for i in range(2, n):
        memo.append(memo[-1] + memo[-2])
        
    print(memo[-1]%10007)