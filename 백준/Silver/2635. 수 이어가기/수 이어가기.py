import sys;
n = int(sys.stdin.readline().rstrip());

max_len = -1;
max_lst = [];

for i in range(n//2, n+1):
    first = n;
    second = i;
    lst = [first, second]

    while True:
        next = first-second;

        if next < 0:
            break;
        else:
            lst.append(next);
            first = second;
            second = next;



    if len(lst) > max_len:
        max_len = len(lst);
        max_lst = lst;


print(max_len);
for i in max_lst:
    print(i, end=" ");

