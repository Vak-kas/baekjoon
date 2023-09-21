from collections import deque;
import sys;

n, k = map(int, sys.stdin.readline().split());
queue = [str(i) for i in range(1, n+1)]
ans = [];
# print(queue);

index = 0;

while True:
    if len(queue) == 0:
        break;
        
    index+=k-1;
    index%=n;
    
    tmp = queue.pop(index);
    # print(tmp);
    ans.append(tmp);
    n-=1;
    
    # print(ans);
    
print("<", end="");
print(", ".join(ans), end="");
print(">");
        