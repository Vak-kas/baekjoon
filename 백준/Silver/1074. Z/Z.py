import sys;

n, r, c = map(int, sys.stdin.readline().split());

k = 2**n -1; #행, 열의 사이즈
row_start = 0; #행 시작
col_start = 0; #열 시작

row_end = k; #행 끝
col_end = k; # 열 끝

row_center = (row_start + row_end)//2; #행의 중간 
col_center = (col_start + col_end)//2; #열의 중간 

num_min = 0; #번호 시작
num_max = 2**n * 2**n -1; #번호 끝 
num_center = (num_min + num_max)//2; #번호 중간

count = 0; #종료 조건을 위한 카운트


#계산 시작
while True:        
    if r<=row_center: #행 중간 지역보다 r 이 작으면
        row_end = row_center; #행 끝 부분을 행 중간부분으로 절반을 줄임
        num_max = num_center; #번호 최대 범위도 절반 줄임

    else:  #행 중간 지역보다 r이 크면
        row_start = row_center+1; #행 시작부분을 행중간 +1로 바꿈
        num_min = num_center+1; # #번호 시작부분도 중간 부분으로 옮겨줌

        
    row_center = (row_start + row_end)//2; #행 중앙 값 다시 계산
    num_center = (num_min + num_max)//2 #번호 중앙 값 다시 계산
    
    # print(f"{num_min} ~ {num_max}")
        
    
    # 행 계산 한 것 처럼 열 계산 똑같이 계산
    if c<=col_center:
        col_end = col_center;
        num_max = num_center;

    else:
        col_start = col_center+1;
        num_min = num_center+1;

    col_center = (col_start + col_end)//2;
    num_center = (num_min + num_max)//2
    
    # print(f"{num_min} ~ {num_max}")    
        
    
    #종료 조건, n만큼
    count+=1;
    if count >=n:
        break;
        
print(num_min);
    
    
    
    
    