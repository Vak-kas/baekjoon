import sys;
from queue import PriorityQueue;

n = int(sys.stdin.readline().rstrip());
lst = PriorityQueue();
s = 0;
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    lst.put(tmp);
    
while True:
    if lst.qsize() == 1:
        break;
    else:
        value1 = lst.get();
        value2 = lst.get();
        # print(value1, value2);
    
        lst.put(value1+value2);
        s += value1 + value2;
        # print(lst);
        
print(s);
            
            