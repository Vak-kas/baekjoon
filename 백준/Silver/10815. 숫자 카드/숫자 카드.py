import sys;
n = int(sys.stdin.readline().rstrip());
have = set(map(int, sys.stdin.readline().split()));


k = int(sys.stdin.readline().rstrip());

want = list(map(int, sys.stdin.readline().split()));

for i in want:
    if i in have:
        print(1, end=" ");
    else:
        print(0, end=" ");


