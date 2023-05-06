import sys;
import math;

# def factorial(n):
#     if n==1:
#         return 1;
#     s =n * factorial(n-1);
#     # print(s);
    
#     return s;

n = int(sys.stdin.readline().rstrip());



for i in range(n):
    a, b = (map(int, sys.stdin.readline().split()));
    

    k = math.factorial(a);

    l = math.factorial(b);
    m = math.factorial(b-a)

    print(int(l/(k*m)));
