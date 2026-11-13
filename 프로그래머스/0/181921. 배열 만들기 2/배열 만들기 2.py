def solution(l, r):
    answer = []
    for i in range(l, r+1):
        tmp = set(str(i))
        tmp.discard("5")
        tmp.discard("0")
        if len(tmp):
            continue
        else:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    return answer