from heapq import *;
import sys;
lst = [];
n = int(sys.stdin.readline().rstrip());

for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    if tmp == 0:
        try:
            print(heappop(lst)[1]);
        except:
            print(0);
    else:
        heappush(lst, (-tmp, tmp));
        

