import sys;

row, col, inven = map(int, sys.stdin.readline().split());
lst = []
for i in range(row):
    k = list(map(int, sys.stdin.readline().split()));
    lst+=k;

lst.sort(reverse = True);
# print(lst);
top, bottom = max(lst), min(lst);
# print(bottom, top)

ans = [];


for height in range(bottom-1, top+1):
    if height <0:
        continue;
        
    flag = True;
    time = 0;
    item = inven;
    for i in range(len(lst)):
        if lst[i] >height:
            a = lst[i] - height;
            time +=2*a
            item +=a;
        elif lst[i] < height:
            a = height - lst[i]
            item -=a;
            time +=a
    if item <0:
        flag = False;

                
    if flag:
        ans.append((time, height));
# print();
# print(ans);
            

ans = sorted(ans, key = lambda x:(x[0], -x[1]));


print(ans[0][0], ans[0][1])
