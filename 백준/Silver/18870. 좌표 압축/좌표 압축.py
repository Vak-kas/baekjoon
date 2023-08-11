import sys;
from heapq import *;

n = int(sys.stdin.readline());

tmp = list(map(int, sys.stdin.readline().split()))
lst=[];
for i in range(n):
    lst.append((tmp[i], i));
    

ans = [0]*n;

lst.sort();

num = 0;
recent = lst[0][0]

for i in range(n):
    now = heappop(lst)
    now_value = now[0];
    index = now[1];
    
    if recent == now_value:
        ans[index] = num;
    else:
        num+=1;
        ans[index] = num;
        recent = now_value;
    
for i in ans:
    print(i, end=" ");