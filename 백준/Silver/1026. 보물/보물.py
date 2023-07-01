import sys;
n=int(sys.stdin.readline().rstrip());

a = list(map(int, sys.stdin.readline().split()));
b = list(map(int, sys.stdin.readline().split()));

a.sort();
b.sort(reverse = True);

value = 0;
for i in range(n):
    value  += a[i]*b[i]
    
print(value)