import sys;
n, m = map(int, sys.stdin.readline().split()); #n, m 입력
 
a = set(map(int, sys.stdin.readline().split())) #a 집합 입력
b = set(map(int, sys.stdin.readline().split())); #b 집합 입력

print(len(a-b)+len(b-a)) #각 집합의 차를 구한 후 길이를 더해서 계산
