import sys;
from heapq import *;

city = int(sys.stdin.readline().rstrip());
bus = int(sys.stdin.readline().rstrip());
edgeList = [[]  for i in range(city+1)];
for i in range(bus):
    start, end, weight = map(int, sys.stdin.readline().split());
    edgeList[start].append((end, weight));
    
start, end = map(int, sys.stdin.readline().split());

visited = [False for _ in range(city+1)];
visited[0] = True;
max_value = 2100000000;
lst = [max_value for _ in range(city+1)]
lst[start] = 0;


q = [];
heappush(q, (0, start))
# visited[start] = True;

while len(q)>0:
    value, now = heappop(q);
    # print(value, now)


    if visited[now] == False:
        visited[now] = True;
        for next, next_weight in edgeList[now]:
            lst[next] =min(next_weight + lst[now], lst[next]);

            heappush(q, (lst[next], next))
        
        
print(lst[end])
# print(lst)
        
        
        
    