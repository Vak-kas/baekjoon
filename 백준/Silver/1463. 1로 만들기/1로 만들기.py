import sys;

n = int(sys.stdin.readline().rstrip());

Memoization = [0 for _ in range(n+1)];
Memoization[0] = 9999999
if n<2:
    pass
else:
    for i in range(2, n+1):
        value1, value2, value3 = 0, 0, 0;
        index = i;
        if index%3==0:
            value1 = index//3;
        if index%2==0:
            value2 = index//2;
        value3 = index-1;
        value = min(Memoization[value1], Memoization[value2], Memoization[value3])
        # print(value1, value2, value3, value)
        Memoization[i] = 1+value
        # print(f"{i} --> {Memoization[i]}")
print(Memoization[n])

    