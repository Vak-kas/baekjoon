import sys;

n, k = map(int, sys.stdin.readline().split());

lst = [True for _ in range(n+1)]; #0번 인덱스부터 n번 인덱스까지 배열 생성
lst[0] = False; #0은 소수가 아니므로 false
lst[1] = False; #1은 소수가 아니므로 false

count = 0;
flag = False;
for i in range(2, n+1):
    if lst[i] == False: #False 가 되어있다 -> 이미 지워진 숫자라는 의미이므로 pass;
        continue;
        
    for j in range(i, n+1, i): #p 만큼 더해주면서 p의 배수인 값들을 전부 돌면서
        if lst[j] == True: #아직 지워지지 않은 수라면
            count+=1; #카운트 세고
            lst[j] = False; #지워줌
            
            if count == k: #k 번째로 지워진 값이 나오면
                flag = True;
                result = j; #해당 값 result 변수에 넣고 종료
                break;
                
    if flag: #종료 조건이 나오면 종료
        break;
            
            
print(result)
    
    
        
    
