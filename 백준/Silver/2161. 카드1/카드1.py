from collections import deque;
import sys;
n = int(sys.stdin.readline().rstrip());
lst = [i for i in range(1, n+1)]
q = deque(lst);

result = [None]*n;

flag = True;
idx = 0;
while True:
    now = q.popleft();
    if flag:
        result[idx] = now;
        idx+=1;
        flag = False;
    else:
        q.append(now);
        flag = True;
        
    
    if idx >=n:
        break;
        
for i in result:
    print(i, end=" ");
        
    
    


