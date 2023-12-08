import sys;

s = sys.stdin.readline().rstrip(); #문자열 s 입력

lst = [s[i:] for i in range(len(s))] #앞자리를 한 자리씩 줄인 값을 리스트에 차례대로 넣기
lst.sort(); #사전순으로 정렬

for i in lst:
    print(i); #출력