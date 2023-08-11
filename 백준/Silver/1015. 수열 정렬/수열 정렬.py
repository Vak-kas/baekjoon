import sys;

n = int(sys.stdin.readline().rstrip());

tmp = list(map(int, sys.stdin.readline().split()));
lst = [];
for i in range(n):
    lst.append((tmp[i], i));
lst.sort();
# print(lst)
num = 0;
ans = [0]*n;
for i in range(n):
    now_value = lst[i][0];
    now_index = lst[i][1];
    
    ans[now_index] = num;
    num+=1;
    
for i in ans:
    print(i, end=" ");