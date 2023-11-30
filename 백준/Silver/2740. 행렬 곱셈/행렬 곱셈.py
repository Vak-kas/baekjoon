import sys;


row1, col1 = map(int, sys.stdin.readline().split());
a = [];

for i in range(row1):
    tmp = list(map(int, sys.stdin.readline().split()));
    a.append(tmp);
    
# print(a)


row2, col2 = map(int, sys.stdin.readline().split());
b = [[] for _ in range(col2)]
for i in range(row2):
    lst = list(map(int, sys.stdin.readline().split()))
    
    for j in range(len(lst)):
        b[j].append(lst[j])
        
        
# print(b)
# c = [[0 for _ in range(col2)] for _ in range(row1)];
# print(c);
# tmp = [];
result = [];
for i in range(len(a)):
    tmp = []
    p = a[i];
    for j in range(len(b)):
        s = 0;
        q = b[j];
        
        for k in range(len(a[i])):
            s+=p[k] * q[k];
            
            
        tmp.append(s);
    result.append(tmp);
        
        
# print(result);
        

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=" ");
        
    print();
        
        
        