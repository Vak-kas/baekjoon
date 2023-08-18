import sys;

n = sys.stdin.readline().rstrip();
lst = [0]*26

for i in n:
    lst[int(ord(i))-97]+=1;
# print(int(ord("a")));

for i in lst:
    print(i, end=" ");