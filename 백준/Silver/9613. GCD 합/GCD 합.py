import sys;
import math;

n = int(sys.stdin.readline().rstrip()); 

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()));
    del lst[0];
    
    s = 0;
    for i in range(0, len(lst)-1):
        for j in range(i+1, len(lst)):
            s+=math.gcd(lst[i], lst[j]);
            
    print(s);
            
            
    