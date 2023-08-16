import sys;

from collections import deque;

def printList(lst):
    global row, col;
    for i in range(1, row+1):
        for j in range(1, col+1):
            print(lst[i][j], end=" ");
        print();

def BFS(pos, count):
    global visited, earth, land, row, col
    start_x = pos[0];
    start_y = pos[1];
    visited[start_x][start_y]  = True;
    queue = deque();
    queue.append((start_x, start_y))
    
    land[start_x][start_y] = count;
    
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    
    while len(queue)>0:
        now = queue.popleft();
        now_x = now[0];
        now_y = now[1];
        
        for i in range(8):
            tmp_x = now_x + dx[i];
            tmp_y = now_y + dy[i];
            
            if visited[tmp_x][tmp_y] == 0 and earth[tmp_x][tmp_y] == 1:
                queue.append((tmp_x, tmp_y));
                land[tmp_x][tmp_y] = count;
                visited[tmp_x][tmp_y] = True;
                
                
    

while True:
    col, row = map(int, sys.stdin.readline().split());
    if col == 0 and row == 0:
        break;
        
    earth = [[0 for _ in range(col+2)] for _ in range(row+2)]
    visited = [[False for _ in range(col+2)] for _ in range(row+2)];
    land = [[0 for _ in range(col+2)] for _ in range(row+2)];
    
    for i in range(1, row+1):
        tmp = list(map(int, sys.stdin.readline().split()));
        
        for j in range(1, col+1):
            earth[i][j] = tmp[j-1]
    # printList(earth)
    # print();
            
    count = 1;
    for i in range(1, row+1):
        for j in range(1, col+1):
            if earth[i][j] == 1 and visited[i][j] == False:
                BFS((i, j), count);
                count+=1;
                
    print(count-1);