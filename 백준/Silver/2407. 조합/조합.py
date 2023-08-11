import sys;

n, r = map(int, sys.stdin.readline().split());

tmp1=1;
tmp2=1;

for i in range(n, n-r , -1):
    tmp1*=i;
    
for i in range(1, r+1):
    tmp2*=i;
    
value = tmp1//tmp2
    
print(value)