import sys;

count = {} #0~9 까지 딕셔너리 생성하기
for i in range(10): #0~9 까지 키값 생성 후, value 값은 0으로 생성
    count[i] = 0;
    
    
n = str(sys.stdin.readline().rstrip()); #방 번호 입력 (문자열로 입력)

for i in n:
    tmp = int(i); #앞 자리부터 차례대로 확인, 단 정수형으로 바꿔줄 것
    

    count[tmp] +=1; #딕셔너리에 키값에 해당하는 value 값 +1로 개수 카운트
        
        
# 6과 9의 값 조정
s = 0; 
#6의 개수와 9의 개수를 더해주고 2로 나누어준 값을 각각 6의 개수와 9의 개수에 나누어줌
s+=count[6];
s+=count[9];
count[6] = s//2;
count[9] = s-count[6];
        

result = list(count.items()); #딕셔너리를 리스트로 변경 후
# print(result)
result.sort(key = lambda x : x[1], reverse=True); #개수가 큰 순서대로 내림차순 정렬
print(result[0][1]);

