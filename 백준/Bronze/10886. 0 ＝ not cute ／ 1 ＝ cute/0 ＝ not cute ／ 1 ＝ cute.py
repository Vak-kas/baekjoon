import sys;

n = int(sys.stdin.readline().rstrip());
c1 = 0;
c0 = 0;
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    if tmp == 0:
        c0 +=1;
    else:
        c1 +=1;
        
if c0>c1:
    print("Junhee is not cute!");
else:
    print("Junhee is cute!");
    
