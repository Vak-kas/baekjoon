def solution(my_string, overwrite_string, s):
    answer = []
    answer +=my_string
    answer[s:len(overwrite_string)+s] = overwrite_string
    answer = "".join(answer)
    return answer