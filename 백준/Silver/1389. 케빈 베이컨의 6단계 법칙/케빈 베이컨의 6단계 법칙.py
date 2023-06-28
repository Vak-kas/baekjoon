import sys;
def printList(edgeList):
    global node;
    
    for i in range(1, node+1):
        print(f"{i} --> {edgeList[i]}")
        
def DFS(x):
    from collections import deque;
    global node, edgeList;
    visited = [-1 for _ in range(node+1)]
    
    queue = deque();
    current = x;
    queue.append(current);
    visited[current] =0;

    
    while queue:
        current = queue.popleft();
        
        for i in edgeList[current]:
            if visited[i] == -1:
                visited[i] = visited[current]+1;
                queue.append(i);
                
    return sum(visited)+1
        

        
    
    
    
    
    

node, link = map(int, sys.stdin.readline().split());

edgeList = [[] for _ in range(node+1)];
for i in range(link):
    a, b = map(int, sys.stdin.readline().split());
    edgeList[a].append(b);
    edgeList[b].append(a);

# printList(edgeList);
min_val = 999;
index = -1;
for i in range(1, node+1):
    tmp = DFS(i);
    if tmp < min_val:
        min_val = tmp;
        index = i
        
print(index);

    