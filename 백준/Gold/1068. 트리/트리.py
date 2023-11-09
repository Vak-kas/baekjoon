import sys;
from collections import deque;

#엣지 리스트 출력
def printEdge(edgeList):
    for i in range(len(edgeList)):
        print(f"{i} -- > {edgeList[i]}")

#엣지리스트 생성
def makeEdge(lst):
    global edgeList, root;
    
    for i in range(len(lst)):
        if lst[i] == -1:
            root = i;
        else:
            edgeList[lst[i]].append(i);
            
def reviseEdge(delete_node):
    global lst, edgeList, root;
    
    if delete_node == -1:
        root = -1;
        return
    
    parent = lst[delete_node];
    edgeList[parent].remove(delete_node);
    
            
def DFS(v):
    global count, edgeList, visited
    visited[v] = True;
    
    if len(edgeList[v]) == 0:
        count+=1;
        return;
    
    for i in edgeList[v]:
        if visited[i] == False:
            DFS(i);
        
    

    

node = int(sys.stdin.readline().rstrip());
lst = list(map(int, sys.stdin.readline().split()));
delete_node = int(sys.stdin.readline().rstrip());

edgeList = [[] for _ in range(node)]; #엣지리스트 생성
visited = [False for _ in range(node)]; #방문리스트 생성
root = -1;
count = 0;
makeEdge(lst);


if delete_node == root:  
    print(0);
    
else:
    reviseEdge(delete_node);
    DFS(root);
    print(count);
    
    
    

