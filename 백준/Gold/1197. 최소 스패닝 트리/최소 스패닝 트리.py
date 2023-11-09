import sys;
# 파인드 함수
def find(a):
    global lst;
    if lst[a] != a:
        lst[a] = find(lst[a]);
        return lst[a];
    return a;



#유니온 함수
def union(a, b):
    global lst
    if a>b:
        a, b = b, a;
        
    uset = find(a);
    vset = find(b);
    
    if uset!=vset:
        lst[b] = a;
    

def printEdge(edgeList):
    for i in range(1, len(edgeList)):
        print(f"{i} --> {edgeList[i]}")


def MST(edgeList):
    global node, lst
    ary = [];
    for i in range(1, len(edgeList)):
        for j in edgeList[i]:
            ary.append((i, j[0], j[1]));
            
    ary.sort(key = lambda x : x[2]);
    
    # print(ary);
    
    index = 0;
    w = 0;
    
    newary = [];
    while len(newary) < node and index < len(ary):
        start, end, weight = ary[index];
        
        a = find(start);
        b = find(end);
        
        if a!=b:
            union(a, b);
            newary.append((ary[index]));
        index+=1;
        
        
    # print(newary);
    for i in newary:
        w+=i[2];
    return w;
        
        
    
    
    
    
        
        
node, edge = map(int, sys.stdin.readline().split());
edgeList = [[] for _ in range(node+1)]
lst = [i for i in range(node+1)];

for i in range(edge):
    start, end, weight = map(int, sys.stdin.readline().split());
    edgeList[start].append((end, weight));
    
# printEdge(edgeList)
w = MST(edgeList);
print(w);
# print(lst);

    
    
