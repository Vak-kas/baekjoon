import sys;
from collections import deque;

n, w, l = map(int, sys.stdin.readline().split());
max_value = 999999;
weight = list(map(int, sys.stdin.readline().split()));
weight.append(max_value)
weight = deque(weight);
# print(weight)


time = [0 for _ in range(w*n+2)]
time[0] = -1;

idx = 1;
flag = False;

while len(weight):
    if flag == False:
        now = weight.popleft(); #다리에 트럭이 꽉 차 있지 않는 경우
    else:
        now = now;  # 다리에 트럭이 꽉 차 있는 경우 이전 now 그대로 사용
        
    if now == max_value:
        break;
    # print(now);
    # print(weight);
    
    if time[idx] + now <= l: # 현재 다리 위에 있는 트럭의 무게 + 새로 뽑은 트럭의 무게
        flag = False;
        
        for i in range(idx, idx+w): #다리 길이 만큼 전부 무게에 +;
            time[i] +=now;
            # print(time[i]);
               
    else: # 현재 뽑은 것을 추가했을 때 다리 최대 하중보다 클 경우
        flag = True; #다음 거 뽑기 패스
        
    idx+=1;
# print(time);


for i in range(len(time)):
    if time[i] == 0:
        print(i)
        break;

