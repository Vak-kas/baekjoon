import sys;
    
from collections import deque;

def printList(lst):
    global row, col;
    for i in range(1, row+1):
        for j in range(1, col+1):
            print(lst[i][j], end=" ");
        print();
    print()
    
def printEveryList(lst):
    global row, col
    for i in range(row+2):
        for j in range(col+2):
            print(lst[i][j], end= " ");
        print();
    print();
    
    
    
def BFS():
    dx = [0, 0, -1, 1];
    dy = [1, -1, 0, 0];

    global row, col, time, box, visited
    
    
    while len(queue)>0:
        now = queue.popleft();
        now_x = now[0];
        now_y = now[1];
        visited[now_x][now_y] = True;
        
        for w in range(4):
            tmp_x = now_x + dx[w];
            tmp_y = now_y + dy[w];
            
            if box[tmp_x][tmp_y] == 0 and visited[tmp_x][tmp_y] == False:
                queue.append((tmp_x, tmp_y))
                visited[tmp_x][tmp_y] = True;
                if time[tmp_x][tmp_y] == 0:
                    time[tmp_x][tmp_y] = time[now_x][now_y]+1;  
                else:
                    time[tmp_x][tmp_y] = min(time[now_x][now_y] + 1, time[tmp_x][tmp_y]);
                    
    
col, row = map(int, sys.stdin.readline().split());

box = [[-1 for _ in range(col+2)] for _ in range(row+2)];
visited = [[False for _ in range(col+2)] for _ in range(row+2)]
time = [[0 for _ in range(col+2)] for _ in range(row+2)]
for i in range(1, row+1):
    tmp = list(map(int, sys.stdin.readline().split()));
    for j in range(1, len(tmp)+1):
        box[i][j] = tmp[j-1]
queue = deque();
for i in range(1, row+1):
    for j in range(1, col+1):
        if box[i][j] == 1:
            queue.append((i, j));
        
BFS()
            
# printList(time)
result = max(map(max, time))
for i in range(1, row+1):
    for j in range(1, col+1):
        if time[i][j] == 0 and box[i][j]==0:
            result = -1;
            break;

    
print(result);