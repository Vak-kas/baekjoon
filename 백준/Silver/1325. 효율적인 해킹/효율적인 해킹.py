import sys

def printEdgeList(array):
    for i in range(1, len(array)):
        print(f"{i} --> {array[i]}")


def BFS(x):
    global edgeList, ans;
    from collections import deque;
    visitedAry = [False for _ in range(node+1)];
    queue = deque();
    current = x;
    queue.append(current)
    visitedAry[current] = True
    while queue:
        current = queue.popleft();
        
        for i in edgeList[current]:
            if not visitedAry[i]:
                queue.append(i);
                visitedAry[i] = True;
                ans[x-1] +=1;

        
    
    

node, repeat = map(int, sys.stdin.readline().split());
edgeList = [[] for _ in range(node+1)];
for i in range(repeat):
    a, b = map(int, sys.stdin.readline().split());
    edgeList[b].append(a);
    
    

    
# printEdgeList(edgeList)
ans= [0 for _ in range(node)]
for i in range(1, node+1):
    BFS(i);

    
maxVal = 0;
for i in range(node):
    maxVal = max(maxVal, ans[i]);

for i in range(len(ans)):
    if maxVal == ans[i]:
        print(f"{i+1}", end=" ");
    
    
    
    