def solution(a, b, c, d):
    answer = 0
    tmp = [a, b, c, d]
    dic = {}
    for i in tmp:
        dic[i] = tmp.count(i)
        
        
    count = len(dic.keys())
    if count == 1:
        answer = 1111*a
    elif count == 2:
        key1, key2 = dic.keys()
        value1 = dic.get(key1)
        value2 = dic.get(key2)
        if value1 == value2:
            answer = (key1 + key2) * abs(key1 - key2)
        else:
            if value1 > value2:
                answer = (10*key1 + key2)**2
            else:
                answer = (10*key2 + key1)**2
    elif count == 3:
        answer = 1
        for i in dic.keys():
            if dic.get(i) == 1:
                answer *= i
    else:
        answer = min(dic.keys())
    
        
    
    return answer