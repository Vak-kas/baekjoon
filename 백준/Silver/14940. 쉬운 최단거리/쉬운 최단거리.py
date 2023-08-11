import sys;
from collections import deque;


row, col = map(int, sys.stdin.readline().split());

def printList(lst):
    for i in range(1, row+1):
        for j in range(1, col+1):
            print(lst[i][j], end=" ");
            
        print();
    print();
    
def printEveryList(lst):
    for i in range(row+2):
        for j in range(col+2):
            print(lst[i][j], end=" ");
            
        print();
    print();
def BFS(start):
    queue = deque();
    queue.append(start);
    visited[start[0]][start[1]] = True;
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0];
    
    while len(queue)>0:
        now = queue.popleft();
        now_x = now[0];
        now_y = now[1];
        
        for i in range(4):
            tmp_x = now_x + dx[i];
            tmp_y = now_y + dy[i];
            
            if visited[tmp_x][tmp_y]  == False and lst[tmp_x][tmp_y] !=0:
                queue.append((tmp_x, tmp_y));
                visited[tmp_x][tmp_y] = True;
                if depth[tmp_x][tmp_y] == 0:                
                    depth[tmp_x][tmp_y] = depth[now_x][now_y] +1;
                else:
                    depth[tmp_x][tmp_y] = min(depth[tmp_x][tmp_y], depth[now_x][now_y]+1)
        
    
    
    
lst = [[0 for _ in range(col+2)] for _ in range(row+2)];
visited = [[False for _ in range(col+2)] for _ in range(row+2)];
depth = [[0 for _ in range(col+2)] for _ in range(row+2)];
start = 0;
for i in range(1, row+1):
    tmp = list(map(int, sys.stdin.readline().split()));
    for j in range(1, len(tmp)+1):
        lst[i][j] = tmp[j-1];
        if tmp[j-1] == 2:
            start = (i, j);


# print();
BFS(start);


for i in range(1, row+1):
    for j in range(1, col+1):
        if depth[i][j] == 0 and lst[i][j] == 1:
            depth[i][j] = -1;
            
printList(depth)
        
