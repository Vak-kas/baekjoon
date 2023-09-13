num1 = set([i for i in range(1, 31)]) #1부터 30까지를 집합으로 넣기
num2 = set([]); # 공집합 만들기

for i in range(28):
    a = int(input()); #값을 입력받고
    num2.add(a);    # 공집합에 넣기
    
    
num3 = list(num1-num2); #차집합을 구한 후, 리스트로 변환하여 num3에 넣기

num3.sort(); #num3 정렬하기

for i in num3:
    print(i);   #num3 출력하기
    


    