def solution(arr, queries):
    answer = []
    for a, b, c, in queries:
        tmp = arr[a:b+1]
        min_value = 999999999
        for i in tmp:
            if i > c:
                if i < min_value:
                    min_value = i

        if min_value != 999999999:
            answer.append(min_value)
        else:
            answer.append(-1)

    return answer
