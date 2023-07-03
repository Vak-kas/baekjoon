import sys;
from collections import deque;

def printEdgeList(edgeList):
    for i in range(1, len(edgeList)):
        print(f"{i} --> {edgeList[i]}")

def printList(lst):
    n = len(lst)
    for i in range(1, n):
        print(lst[i], end=" ");
    print();

building = int(sys.stdin.readline().rstrip());
time = [0 for _ in range(building+1)];
indegree = [0 for _ in range(building+1)]
ans = [0 for _ in range(building+1)];
edgeList = [[] for _ in range(building+1)]
for i in range(1, building+1):
    lst = list(map(int, sys.stdin.readline().split()));
    lst.pop();
    
    time[i] = lst[0];
    del lst[0];
    
    n = len(lst);
    indegree[i] = n;
    
    for j in lst:
        edgeList[j].append(i);
        

# printEdgeList(edgeList);
# printList(time);
# printList(indegree)
# printList(ans);

queue = deque()
seq = [];

for i in range(1, building+1):
    if indegree[i] == 0:
        seq.append(i);
        queue.append(i)
        

while queue:
    now = queue.popleft();
    
    for i in edgeList[now]:
        indegree[i]-=1;
        
        ans[i] = max(ans[i], ans[now] + time[now])
        if indegree[i] == 0:
            queue.append(i);
        
    

        
            
for i in range(1, building+1):
    ans[i] +=time[i]
    print(ans[i])
    
    