import sys;

n = int(sys.stdin.readline().rstrip());
lst = [];
for i in range(n):
    age, name = map(str, sys.stdin.readline().split());
    age = int(age);
    lst.append([age, name, i]);
    
ans = sorted(lst, key  = lambda x:(x[0], x[2]));

for i in range(n):
    print(ans[i][0], ans[i][1]);