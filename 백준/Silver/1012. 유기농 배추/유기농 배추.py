import sys;
from collections import deque;


def printEveryList(lst):
    global row, col;
    for i in range(row+2):
        for j in range(col+2):
            print(lst[i][j], end="  ");
        print();
        
def printList(lst):
    global row, col;
    for i in range(1, row+1):
        for j in range(1, col+1):
            print(lst[i][j], end="  ");
        print();
def DFS():
    global row, col, visitedAry, lst, count;
    for i in range(1, row +1):
        for j in range(1, col+1):
            if lst[i][j] == 1 and visitedAry[i][j] == 0:
                # print(f"{i} {j}");
                count+=1;
                queue.append((i, j));
                visitedAry[i][j] = 1;

                while len(queue)>0:
                    now = queue.popleft();
                    for x in range(4):
                        tmp_x = now[0] + dx[x];
                        tmp_y = now[1] + dy[x];

                        if lst[tmp_x][tmp_y] == 1 and visitedAry[tmp_x][tmp_y] == 0:
                            visitedAry[tmp_x][tmp_y] =1;
                            queue.append((tmp_x, tmp_y));
        

n = int(sys.stdin.readline().rstrip());

for i in range(n):
    row,col,  repeat = map(int, sys.stdin.readline().split());
    
        
    lst = [[0 for _ in range(col+2)] for _ in range(row+2)];
    visitedAry = [[0 for _ in range(col+2)] for _ in range(row+2)];

    for i in range(repeat):
        a, b = map(int, sys.stdin.readline().split());
        lst[a+1][b+1] = 1;
        # printList(lst);

    # printEveryList(lst);
    # print()
    # printList(lst);

    count = 0;
    queue = deque();
    dx = [0, 0, -1, 1];
    dy = [1, -1, 0, 0]



    DFS();
    print(count);
                


