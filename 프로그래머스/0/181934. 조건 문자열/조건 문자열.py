def solution(ineq, eq, n, m):

    answer = int(eval(f"{n}{ineq}{eq}{m}".replace("!", "")))
        
    return answer

