import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mbti = list(input().rstrip().split())
    # 비둘기집 원리
    if N > 32:
        print(0)
    else:
        # Brute Force
        minNum = sys.maxsize
        for x in range(N):
            for y in range(N):
                for z in range(N):
                    if x == y or y == z or x == z:
                        continue
                    cnt = 0
                    for i in range(4):
                        if mbti[x][i] != mbti[y][i]: cnt += 1
                        if mbti[x][i] != mbti[z][i]: cnt += 1
                        if mbti[y][i] != mbti[z][i]: cnt += 1
                    minNum = min(minNum,cnt)
                    
        print(minNum)