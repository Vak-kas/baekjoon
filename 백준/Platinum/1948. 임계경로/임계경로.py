import sys;
from collections import deque;
def printEdge(edgeList):
    for i in range(1, city+1):
        print(f"{i} --> {edgeList[i]}")
    print();
    
def printInfo(lst):
    for i in range(1, city+1):
        print(lst[i], end=" ");
    print();
        

city = int(sys.stdin.readline().rstrip());
road = int(sys.stdin.readline().rstrip());

indegree = [0 for _ in range(city+1)];
time = [0 for _ in range(city + 1)];

edgeList = [[] for _ in range(city+1)]
reverseEdgeList = [[] for _ in range(city+1)]
for i in range(road):
    a, b, c = map(int, sys.stdin.readline().split());
    edgeList[a].append((b, c));
    reverseEdgeList[b].append((a, c));
    indegree[b] +=1;
    
start, end = map(int, sys.stdin.readline().split());
queue = deque();
queue.append(start);

while queue:
    now = queue.popleft();
    
    for next in edgeList[now]:
        next_index = next[0];
        next_time = next[1];
        
        indegree[next_index]-=1;
        if indegree[next_index] ==0:
            queue.append(next_index);
            
        time[next_index] = max(time[next_index], next_time + time[now])
            
        
        

    
# printEdge(edgeList);
# printEdge(reverseEdgeList)
# printInfo(indegree)
# printInfo(time);

print(time[-1])
count = 0;

queue.clear();
visited = [False]*(city+1);

queue.append(end);
visited[end] = True;

while queue:
    now = queue.popleft();
    for next in reverseEdgeList[now]:
        if time[now] - time[next[0]] == next[1]:
            count+=1;
            if visited[next[0]] == False:
                queue.append(next[0]);
                visited[next[0]] = True;
print(count)