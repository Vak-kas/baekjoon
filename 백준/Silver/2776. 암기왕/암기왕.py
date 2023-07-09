import sys;

n = int(sys.stdin.readline().rstrip());

for _ in range(n):
    k = int(sys.stdin.readline().rstrip());
    lst = set(map(int, sys.stdin.readline().split()));
    
    m = int(sys.stdin.readline().rstrip());
    lst2 = list(map(int, sys.stdin.readline().split()));
    
    for i in lst2:
        if i in lst:
            print(1);
        else:
            print(0);
    
    