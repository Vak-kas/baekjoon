n = 7;

import sys;
lst = []
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    if tmp%2 == 1:
        lst.append(tmp);
        
if len(lst) == 0:
    print(-1);
else:
    print(sum(lst));
    print(min(lst));