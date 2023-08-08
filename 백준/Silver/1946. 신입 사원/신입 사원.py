import sys;
t = int(sys.stdin.readline().rstrip());
for _ in range(t):
    
    n = int(sys.stdin.readline().rstrip());

    lst = [];

    for i in range(n):
        rank1, rank2 = map(int, sys.stdin.readline().split());
        lst.append((rank1, rank2, i));

    first_sort = sorted(lst, key = lambda x : x[0]);
    second_sort = sorted(lst, key = lambda x : x[1]);

    # print(first_sort);
    # print(second_sort);

    count1 = [];
    count2 = set([]);

    max_rank2 = first_sort[0][1];
    for i in first_sort[1:]:
        if i[1] > max_rank2:
            count1.append(i[2]);
        else:
            max_rank2 = i[1];
    max_rank1 = second_sort[0][0];
    for i in second_sort[1:]:
        if i[0] > max_rank1:
            count2.add(i[2]);
        else:
            max_rank1 = i[0];

    count = len(count1) + len(count2);
    # print(count1, count2)

    for i in count1:
        if i in count2:
            count-=1;

    print(n-count);

