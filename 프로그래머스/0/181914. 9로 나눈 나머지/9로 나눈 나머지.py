def solution(number):
    answer = 0
    num = list(map(int, number))
    answer = sum(num)%9
    return answer