def solution(num_list):
    tmp = 1
    for i in num_list:
        tmp*=i
    answer = int(tmp < sum(num_list)**2)
    return answer