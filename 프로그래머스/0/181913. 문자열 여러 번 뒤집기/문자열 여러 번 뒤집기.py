def solution(my_string, queries):
    answer = my_string
    for s, e in queries:
        tmp = answer[s:e+1]
        tmp = tmp[::-1]
        answer = answer[:s] + tmp + answer[e+1:]
        
    return answer