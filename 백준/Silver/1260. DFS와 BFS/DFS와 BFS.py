import sys;
from collections import deque;
from collections import deque

def printEdgeList(edgeList):
    for i in range(1, len(edgeList)):
        print(f"{i} --> {edgeList[i]}");
        
def DFS(i):
    global edgeList;
    # visitedAry = [False for _ in range(node+1)];
    
    seq = [];
    stack = [];
    stack.append(i);
    
    while len(stack)>0:
        tmp = stack.pop();
        # print(tmp, end=" ");
        if tmp not in seq:
            seq.append(tmp);
            for v in edgeList[tmp]:
                # print(v);
                # if v not in seq:
                    stack.append(v);
                    # visitedAry[v] = True;
    for i in seq:
        print(i, end= " ");
    print();
        
def BFS(i):
    global edgeList;
    seq = [];
    dq = deque();
    dq.append(i);
    
    while len(dq)>0:
        tmp = dq.popleft();
        if tmp not in seq:
            seq.append(tmp);
            
            for v in edgeList[tmp]:
                dq.append(v);
                
    for i in seq:
        print(i, end =" ");
    
    
    
                

node, edge, start = map(int, sys.stdin.readline().split());

# visitedAry = [False for _ in range(node+1)];
edgeList = [[] for _ in range(node +1)];

for i in range(edge):
    a, b = map(int, sys.stdin.readline().split());
    edgeList[a].append(b);
    edgeList[b].append(a);
    
for i in edgeList:
    i.sort(reverse=True);

DFS(start);

for i in edgeList:
    i.sort(reverse = False);
    
# printEdgeList(edgeList);
BFS(start)
    


