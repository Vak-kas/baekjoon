def solution(arr, queries):
    answer = arr
    count = 0
    for a, b, c in queries:
        for i in range(len(arr)):
            if i < a or i >b :
                continue
            
            if i%c==0:
                answer[i] +=1
    return answer