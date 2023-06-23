import sys;

n = int(sys.stdin.readline().rstrip());


lst = [666];
if n==1:
    print(666);
else:
    count = 1;
    num = 1665;
    while count != n:
        num+=1;
        tmp = str(num);
        if "666" in tmp and num not in lst:
            count+=1;
            lst.append(num);
                
        
    print(num);
        