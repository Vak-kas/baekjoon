import sys
sys.setrecursionlimit(10000)
def printEdge(edgeList):
    for i in range(1, len(edgeList)):
        print(f"{i} --> {edgeList[i]}")
        
def DFS(i):
    global edgeList, visitedAry, count;
    
    count+=1;
    visitedAry[i] = True;
    for v in edgeList[i]:
        if not visitedAry[v]:
            DFS(v);
    
    
node = int(sys.stdin.readline().rstrip());
edge = int(sys.stdin.readline().rstrip());
count = 0;
edgeList = [[] for _ in range(node+1)]
visitedAry = [False for _ in range(node+1)]


for i in range(edge):
    a, b = map(int, sys.stdin.readline().split());
    edgeList[a].append(b);
    edgeList[b].append(a);
    
# printEdge(edgeList);
DFS(1);
print(count-1);
