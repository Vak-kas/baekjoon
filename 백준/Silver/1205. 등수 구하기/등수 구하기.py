import sys;

n, new_score, p = map(int, sys.stdin.readline().split());
lst = [];
if n>0:
    lst = list(map(int, sys.stdin.readline().split()));

idx = 0;
idx_lst = [];
while idx <n:
    idx_lst.append((idx, lst[idx]))
    idx+=1;
    
idx_lst.append((idx, new_score));
    
sorted_idx_lst = sorted(idx_lst, key = lambda x : (x[1], -x[0]), reverse=True);

# print(sorted_idx_lst);


rank =1;
new_score_index = -1;

now = 1;

for i in sorted_idx_lst:
    if new_score < i[1]:
        rank+=1;
    if new_score == i[1] and idx == i[0]:
        new_score_index = now;
        
    now+=1;
# print(new_score_index);
    
if new_score_index<=p:
    print(rank);
else:
    print(-1);

