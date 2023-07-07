import sys;

def printEdge(edgeList):
    global node
    for i in range(1, node+1):
        print(f"{i} --> {edgeList[i]}")
        

node, edge = map(int, sys.stdin.readline().split());
start_node = int(sys.stdin.readline().rstrip());
edgeList = [[] for _ in range(node+1)]

for i in range(edge):
    start, end, weight = map(int, sys.stdin.readline().split());
    edgeList[start].append((end, weight));
    
# printEdge(edgeList)

INFINITE = sys.maxsize;

distance = [INFINITE for _ in range(node+1)];
visited = [False for _ in range(node +1)];
visited[0]  = True;


from heapq import *;

h = [];
heappush(h, (0, start_node));
# visited[start_node] = True;
distance[start_node] = 0;

while len(h) > 0:
    now = heappop(h);
    now_node = now[1];
    now_value = now[0]
    
    if visited[now_node]:
        continue;
    visited[now_node] = True;
    
    for next, value in edgeList[now_node]:
        distance[next] = min(distance[next], distance[now_node] + value);
        heappush(h, (distance[next], next))

            
# print(visited)
            
for i in range(1, node+1):
    if visited[i]:
        print(distance[i]);
    else:
        print("INF");
    
        