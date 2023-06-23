import sys;

n = int(sys.stdin.readline().rstrip());

lst = [(0, 0, 0)]

for i in range(n):
    weight, height = map(int, sys.stdin.readline().split());
    lst.append((weight, height, i+1))
    
sorted_list = sorted(lst, key = lambda x: (x[0], x[1]), reverse = True);

# print(sorted_list);
rank = 1;
rank_list = [];
for i in range(n):
    for j in range(n):
        if i==j:
            pass;
        if sorted_list[i][0] < sorted_list[j][0] and sorted_list[i][1] < sorted_list[j][1]:
            rank+=1;
            
    
    rank_list.append((rank, sorted_list[i][2]));
    rank = 1;
# print(rank_list);

s_rank = sorted(rank_list, key = lambda x: x[1])

for i in s_rank:
    print(i[0], end=" ");
    
    