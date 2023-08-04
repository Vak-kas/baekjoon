import sys;


n = int(sys.stdin.readline().rstrip());
lst = [];
for i in range(n):
    start, end = map(int, sys.stdin.readline().split());
    lst.append((start, end));

    

sorted_lst = sorted(lst, key = lambda x:(x[1], x[0]))
# print(sorted_lst);

count = 0;
start = 0;
end = 0 ;

for s, e in sorted_lst:

    if s>=end:
        start = s;
        end = e;
        count +=1;
        # print(s, e)
        
print(count);
    
