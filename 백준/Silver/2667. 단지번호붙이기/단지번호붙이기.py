import sys;
from collections import deque;

def printList(lst):
    global n
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(lst[i][j], end=" ");
        print();
        
def BFS(i, count):
    global visited, number, lst, n
    
    start_x = i[0];
    start_y = i[1];
    
    queue = deque();
    queue.append((start_x, start_y));
    visited[start_x][start_y] = True;
    number[start_x][start_y] = count;
    
    dx= [0, 0, -1, 1];
    dy = [1, -1, 0, 0];
    while len(queue)>0:
        now = queue.popleft();
        now_x = now[0];
        now_y = now[1];
        
        for i in range(4):
            tmp_x = now_x + dx[i];
            tmp_y = now_y + dy[i];
            
            if lst[tmp_x][tmp_y] == 1 and visited[tmp_x][tmp_y] == False:
                visited[tmp_x][tmp_y] = True;
                number[tmp_x][tmp_y] = count;
                queue.append((tmp_x, tmp_y));
                
        

n = int(sys.stdin.readline().rstrip());
lst = [[0 for _ in range(n+2)] for _ in range(n+2)];
visited = [[False for _ in range(n+2)] for _ in range(n+2)]
number = [[0 for _ in range(n+2)] for _ in range(n+2)]
for i in range(1, n+1):
    tmp = sys.stdin.readline().rstrip();
    tmp = "0" + tmp + "0";
    for j in range(len(tmp)):
        lst[i][j] = int(tmp[j])
        
count = 1;
for i in range(1, n+1):
    for j in range(1, n+1):
        if lst[i][j] == 1 and visited[i][j] == False:
            BFS((i, j), count);
            count+=1;

    
# printList(number)
# print();
# printList(visited);
ans = [];
print(count-1);
for i in range(1, count):
    s = 0;
    for j in range(1, n+1):
        s+=number[j].count(i)
        # print(s)
        
    ans.append(s);
    
ans.sort();
for i in ans:
    print(i);

