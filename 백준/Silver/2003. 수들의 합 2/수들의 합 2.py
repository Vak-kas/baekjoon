import sys;

n, m = map(int ,sys.stdin.readline().split());
lst = map(int, sys.stdin.readline().split());


sum_lst = [0 for _ in range(n)];

s = 0;
index = 0;
for i in lst:
    s+=i;
    sum_lst[index] = s;
    index+=1;
    
# print(sum_lst)
count = 0;
for i in range(n):
    if sum_lst[i] <m:
        continue;
        
    if sum_lst[i] == m:
        # print(f"{i}번째를 더했다.")
        count+=1;
        continue;
    
    for j in range(i):
        # print(i, j)
        if sum_lst[i] - sum_lst[j] < m:
            break;
        elif sum_lst[i]-sum_lst[j] == m:
            # print(f"{i}번째에서 {j}를 뺐다.")
            count+=1;
            break;
        
print(count)
    
    