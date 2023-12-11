import sys;
max_range = 100;
def printMaze(maze):
    for i in range(1, max_range+1):
        for j in range(1, max_range+1):
            print(maze[i][j], end= " ");
        print();
    
    

maze = [[False for _ in range(max_range+1)] for _ in range(max_range+1)]
# printMaze(maze)
n = int(sys.stdin.readline().rstrip());

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split());
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            maze[i][j] = True;
    
count= 0;
for i in range(1, max_range+1):
    for j in range(1, max_range+1):
        if maze[i][j] == True:
            count+=1;
            
print(count);
        
    