lst = []; #리스트 선언

for i in range(9): # for구문 9번 반복
    a = int(input()); #a입력받고
    lst.append(a); #리스트에 넣기
    
max = -1; #최대값 저장 변수
maxIndex = -1; #최대값 인덱스 저장변수

for i in range(9): #리스트를 돌면서
    if lst[i] > max: #현재 인덱스의 리스트값이 저장되어 있는 최대값보다 크면?
        max = lst[i]; #최대값은 현재 인덱스의 리스트값으로 저장해주고
        maxIndex = i; #최대값 인덱스도 현재 인덱스로 바꿔줌.
        
        
print(max); #최대값 변수 출력
print(maxIndex+1); #문제에서는 인덱스 위치를 물어 본 것이 아니라, 몇 번째 위치냐고 물었으므로, +1을 해줘야함
