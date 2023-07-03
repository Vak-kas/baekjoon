import sys;
sys.setrecursionlimit(1000000)
def find(a):
    global lst;
    if lst[a] == a:
        return a;
    else:
        lst[a] = find(lst[a])
        return lst[a]
    
def union(a, b):
    a = find(a);
    b = find(b);
    if a!=b:
        lst[b] = a;
    

node, calc = map(int, sys.stdin.readline().split());

lst = [i for i in range(node+1)]

for i in range(calc):
    order, a, b = map(int, sys.stdin.readline().split());
    if a>b:
        a, b = b, a;
    if order == 0:
        union(a, b)
        
    else:
        if find(a) == find(b):
            result = "YES";
        else:
            result = "NO";
        print(result);
        
# print(lst);

    