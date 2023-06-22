def factorial(n):
    memo = [1, 1, 2];
    
    if n<3:
        return memo[n];
    
    else:
        mul = 1;
        for i in range(len(memo)):
            mul *=memo[i];
        for i in range(3, n+1):
            mul*=i;
            memo.append(mul);
            
            
    return memo[-1]

def countZero(a):
    n = len(a);

    
    count = 0;
    for i in range(n):
        if a[i] == "0":
            count+=1;
        else:
            return count;


import sys;

n = int(sys.stdin.readline().rstrip());

a = str(factorial(n));
# print(a);
a = a[::-1]
# print(a);

ans = countZero(a);
print(ans);

    