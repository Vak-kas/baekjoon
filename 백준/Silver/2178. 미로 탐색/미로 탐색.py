import sys;
from collections import deque;

def printAry(lst):
    global row, col
    for i in range(1, row+1):
        for j in range(1, col+1):
            print(lst[i][j], end =" ");
        print();
        
def printEvery(lst):
    global row, col;
    for i in range(row+2):
        for j in range(col+2):
            print(lst[i][j], end=" ");
        print();
        
        
def BFS(x, y):
    global row, col, lst, depth, visited;
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0];
    
    queue = deque();
    # print(queue)
    
    queue.append((x, y));
    visited[x][y] = True;
    
    
    while len(queue)>0:
        # print(queue)
        now = queue.popleft();
        
        for i in range(4):
            tmp_x = now[0]+dx[i];
            tmp_y = now[1]+dy[i];
            # print(f"{tmp_x} {tmp_y} -> {lst[tmp_x][tmp_y]}")
            if (lst[tmp_x][tmp_y] ==1) and (visited[tmp_x][tmp_y] == False):
                visited[tmp_x][tmp_y] = True;
                depth[tmp_x][tmp_y] = depth[now[0]][now[1]] +1;
                queue.append((tmp_x, tmp_y));



row, col = map(int, sys.stdin.readline().split());

# 배열 생성
lst = [[0 for _ in range(col+2)] for _ in range(row+2)];

#깊이 생성
depth = [[0 for _ in range(col+2)] for _ in range(row + 2)]

#방문 했으면 True, 방문 안 했으면 False
visited = [[False for _ in range(col+2)] for _ in range(row+2)]
#시작지점 1로 설정
depth[1][1] = 1;

#배열에 입력받은 값 넣기
for i in range(1, row+1):
    tmp= ""
    tmp += (sys.stdin.readline().rstrip());
    # idx = 1;
    # print(tmp)
    for j in range(len(tmp)):
        lst[i][j+1] = int(tmp[j]);
        # idx+=1;
        
#배열 출력
# printAry(lst);
# print();

#배열 전체 출력
# printEvery(lst);

#BFS 실행
BFS(1, 1);

# print()
# printAry(visited);
# print();
# printEvery(depth);


print(depth[row][col])



