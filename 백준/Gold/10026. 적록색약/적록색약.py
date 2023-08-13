import sys;
from collections import deque;

# 적록색맹이 아닌 경우
def BFS1(pos, count):
    global visited1, number1, color, n;
    
    queue = deque();
    start_x = pos[0];
    start_y = pos[1];
    queue.append((start_x, start_y));
    visited1[start_x][start_y] = True;
    number1[start_x][start_y] = count;
    
    dx = [0, 0, -1, 1];
    dy = [1, -1, 0, 0];
    
    while queue:
        now = queue.popleft();
        now_x = now[0];
        now_y = now[1];
        
        for i in range(4):
            tmp_x = now_x + dx[i];
            tmp_y = now_y + dy[i];
            
            if color[tmp_x][tmp_y] != "A" and visited1[tmp_x][tmp_y] == False and color[tmp_x][tmp_y] == color[now_x][now_y]:
                queue.append((tmp_x, tmp_y));
                visited1[tmp_x][tmp_y] = True;
                number1[tmp_x][tmp_y] = count;
                
                
        
        
    
    
# 적록색맹인 경우
def BFS2(pos, count):
    global visited2, number2, color, n;
    
    dx = [0, 0, -1, 1];
    dy = [1, -1, 0, 0]
    queue = deque();
    start_x = pos[0];
    start_y = pos[1];
    queue.append((start_x, start_y));
    visited2[start_x][start_y] = True;
    number2[start_x][start_y] = count;
    
    while queue:
        now = queue.popleft();
        now_x = now[0];
        now_y = now[1];
        
        for i in range(4):
            tmp_x = now_x + dx[i];
            tmp_y = now_y + dy[i];
            # print(tmp_x, tmp_y)
            
            if visited2[tmp_x][tmp_y] == False and color[tmp_x][tmp_y] != "A":
                if color[tmp_x][tmp_y] == color[now_x][now_y]:
                    visited2[tmp_x][tmp_y] = True;
                    queue.append((tmp_x, tmp_y));
                    number2[tmp_x][tmp_y] = count;
                    
                elif color[now_x][now_y] == "R" and color[tmp_x][tmp_y] == "G":
                    visited2[tmp_x][tmp_y] = True;
                    queue.append((tmp_x, tmp_y));
                    number2[tmp_x][tmp_y] = count;
                
                elif color[now_x][now_y] == "G" and color[tmp_x][tmp_y] == "R":
                    visited2[tmp_x][tmp_y] = True;
                    queue.append((tmp_x, tmp_y));
                    number2[tmp_x][tmp_y] = count;
                    
                    
                    
                    
                    
                    
    
    
    

def printList(lst):
    global n
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(lst[i][j], end=" ");
        print();


n = int(sys.stdin.readline().rstrip());

color = [["A" for _ in range(n+2)] for _ in range(n+2)]
visited1 = [[False for _ in range(n+2)] for _ in range(n+2)]
visited2 = [[False for _ in range(n+2)] for _ in range(n+2)]

number1 = [[0 for _ in range(n+2)] for _ in range(n+2)]
number2 = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(1, n+1):
    tmp = "A" + sys.stdin.readline().strip() + "A";
    
    for j in range(len(tmp)):
        color[i][j] = tmp[j];
count = 1;
ans = [];
for i in range(1, n+1):
    for j in range(1, n+1):
        if visited1[i][j] == False:
            BFS1((i, j), count);
            count+=1;
            
ans.append(count-1);
count = 1;
for i in range(1, n+1):
    for j in range(1, n+1):
        if visited2[i][j] == False:
            # print(i, j)
            BFS2((i, j), count);
            count+=1;
            
ans.append(count-1);
            

            
for i in ans:
    print(i, end=" ");