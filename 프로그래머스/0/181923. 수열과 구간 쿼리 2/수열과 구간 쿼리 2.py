def solution(arr, queries):
    answer = []
    for a, b, c, in queries:
        tmp = list(filter(lambda x : x>c, arr[a:b+1]))
        answer.append(min(tmp) if len(tmp) else -1)

    return answer
