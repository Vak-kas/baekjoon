import sys;
import math;

def factorial(n):
    ans = 1;
    
    for i in range(1, n+1):
        ans *=i;
        
    return ans;

n = int(sys.stdin.readline().rstrip());



for i in range(n):
    a, b = (map(int, sys.stdin.readline().split()));
    

    k = factorial(a);

    l = factorial(b);
    m = factorial(b-a)

    print(int(l/(k*m)));
