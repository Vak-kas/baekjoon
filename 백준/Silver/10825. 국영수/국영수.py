import sys;
lst = [];
n = int(sys.stdin.readline().rstrip());
for i in range(n):
    name, kor, end, math = map(str, sys.stdin.readline().split());
    kor = int(kor);
    end = int(end);
    math = int(math)
    lst.append((name, kor, end, math));
    
sort_lst = sorted(lst,key =  lambda x: (-x[1], x[2], -x[3], x[0]));

for i in sort_lst:
    print(i[0])