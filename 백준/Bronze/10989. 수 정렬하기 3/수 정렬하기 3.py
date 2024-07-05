count = {}

import sys;

a = int(sys.stdin.readline().rstrip());

for i in range(a):
    k = int(sys.stdin.readline().rstrip());
    
    if k in count:
        count[k] +=1;
    else:
        count[k] = 1;
        
x = dict(sorted(count.items()))
# print("---")
for i in x:
    for j in range(x[i]):
        print(i)
        



    