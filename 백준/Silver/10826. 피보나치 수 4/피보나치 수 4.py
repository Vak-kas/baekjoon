def fibo(n):
    memo = [0, 1, 1];
    if n<3:
        return memo[n];
    
    else:
        for i in range(3, n+1):
            memo.append(memo[-1] + memo[-2])
            
    return memo[-1];

import sys;

n = int(sys.stdin.readline().rstrip());
print(fibo(n));
            