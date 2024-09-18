from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    count = 0
    for i in tmp:
        if i == "(":
            count+=1
        else:
            if count <=0:
                count = -1
                break
            else:
                count-=1

    if count == 0 :
        print("YES")
    else:
        print("NO")
            

