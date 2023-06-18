import sys;
from collections import deque;

n, compare = map(int, sys.stdin.readline().split())


array = [[] for _ in range(n+1)]
indegree = [0] *(n+1)
ans = [];

for i in range(compare):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)
    indegree[b] +=1;
    
queue = deque();

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i);



while len(queue)>0:
    now = queue.popleft();
    ans.append(now);
    for i in array[now]:
        indegree[i] -=1;
        if indegree[i] == 0:
            queue.append(i);

            
for i in ans:
    print(i, end=" ");
