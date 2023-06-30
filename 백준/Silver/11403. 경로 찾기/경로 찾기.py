import sys;
from collections import deque;

def printList(lst):
    global node
    
    for i in range(node):
        for j in range(node):
            print(lst[i][j], end=" ");
        print();
        
def find_vertex(start):
    global lst, node
    visitedAry= [] ;
    queue = deque();
    queue.append(start);
    # visitedAry.append(start);
    
    while queue:
        current = queue.popleft();
        
        for i in range(node):
            if lst[current][i] ==1 and i not in visitedAry:
                queue.append(i);
                visitedAry.append(i);
        # visitedAry.sort();
    # print(start, visitedAry)
                
    result = [0] * node;
    for i in visitedAry:
        result[i] = 1;
        
    return result
        

node = int(sys.stdin.readline().rstrip());

lst = []


for i in range(node):
    tmp = list(map(int, sys.stdin.readline().split()))
    lst.append(tmp);
    

ans = []
for i in range(node):
    result = find_vertex(i);
    ans.append(result)
    
# print()
printList(ans);
