a = input(); # 문자열 입력받고 a에 넣기

a = a.upper(); #문자열을 전부 대문자로 바꾸기

set_a  = list(set(a)); # a에서 중복되는 알파벳 제거

dic = {} #딕셔너리 생성

for i in set_a:              #딕셔너리에 각 단어의 개수를 입력하기
    dic[i] = a.count(i);
    
sorted_dic = sorted(dic.items(), key = lambda x:x[1], reverse = True) #value 값을 기준으로 정렬하기
# print(sorted_dic);

if len(sorted_dic) == 1:  #정렬된 값의 길이가 하나뿐이라면 ex)zZz 가 입력된 경우, z의 개수만 정렬되기에, 이 값 그대로 출력한다.
    print(sorted_dic[0][0])
#정렬된 값이 2개 이상이라면
else:            
    if sorted_dic[0][1] == sorted_dic[1][1]:     #가장 맨 앞의 알파벳의 개수와 , 2번째로 개수가 많은 알파벳의 개수를 비교하여 같으면
        print("?"); #물음표 출력
    else:     #다르면
        print(sorted_dic[0][0]); #맨 앞의 문자 출력