import sys;

a, b = map(int, sys.stdin.readline().split());

count = 1;
while True:
    
    if b%10 == 1:
        b = b//10;
        # print(b);
        count+=1;
    elif b%2 == 1:
        count = -1;
        break;
        
    else:
        b = b//2;
        count+=1;
        # print(b);
        
    if b==a:
        break;
    
    if b<=0:
        count = -1;
        break;
        
print(count);
    
