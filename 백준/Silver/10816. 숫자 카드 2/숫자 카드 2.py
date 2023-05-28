import sys;

n = int(sys.stdin.readline().rstrip());
lst = list(map(int, sys.stdin.readline().split()));
dic = {};
for i in range(n):
    if lst[i] in dic:
        dic[lst[i]] +=1;
    else:
        dic[lst[i]] = 1;

m  = int(sys.stdin.readline().rstrip());

lst2 = list(map(int, sys.stdin.readline().split()));

for i in range(m):
    try:
        print(dic[lst2[i]], end = " ");
    except:
        print(0, end=" ");
    



