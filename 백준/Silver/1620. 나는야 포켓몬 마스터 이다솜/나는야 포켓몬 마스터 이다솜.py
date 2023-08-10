import sys;
name = {}
num = {}
n, q = map(int, sys.stdin.readline().split());
for i in range(1, n+1):
    a = sys.stdin.readline().rstrip();
    name[a] = i;
    num[i] = a;
    
    
for i in range(q):
    tmp = sys.stdin.readline().rstrip();
    
    try:
        tmp = int(tmp);
        print(num[tmp]);
    except:
        print(name[tmp]);

    