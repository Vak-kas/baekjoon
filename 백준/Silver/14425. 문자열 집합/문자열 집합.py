import sys;
n, m = map(int, sys.stdin.readline().split()); #n, m 입력받기

s = set(); #집합 s 생성

for i in range(n):
    s.add(sys.stdin.readline().rstrip()); #n만큼 반복하면서 입력받은 문자열 집합에 넣기

count = 0; #개수 세는 변수 0으로 초기화

for j in range(m): #m 만큼 돌면서
    if (sys.stdin.readline().rstrip()) in s: #입력받은 문자열이 집합 s에 있는지 확인
        count+=1; #존재하면 개수 count

print(count) #개수 출력
    
    