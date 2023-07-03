import sys;
def printList(lst):
    global city;
    
    for i in range(1, city+1):
        for j in range(1, city+1):
            print(lst[i][j], end=" ");
        print()
    print()
    
def printParent(parent):
    for i in range(1, city+1):
        print(f"{i} --> {parent[i]}")

def find(a):
    if parent[a] == a:
        return a;
    else:
        parent[a] = find(parent[a])
        return parent[a];
    
def union(a, b):
    if a>b:
        a, b = b, a;
    a = find(a);
    b = find(b);
    if a!=b:
        parent[b] = a;
    
city = int(sys.stdin.readline().rstrip());
travel = int(sys.stdin.readline().rstrip());
lst = [[0 for i in range(city+1)]];

parent = [i for i in range(city+1)]

for i in range(city):
    tmp = list(map(int, sys.stdin.readline().split()));
    lst.append([0] + tmp);
    
for i in range(1, city+1):
    for j in range(1, city+1):
        if lst[i][j] == 1:
            union(i, j)
            
plan=list(map(int, sys.stdin.readline().split()));
find_lst = []
for i in plan:
    find_lst.append(find(i));
    
find_lst.sort();

if find_lst[0] != find_lst[-1]:
    print("NO");
else:
    print("YES");

    
    
# printList(lst);
# printParent(parent)
