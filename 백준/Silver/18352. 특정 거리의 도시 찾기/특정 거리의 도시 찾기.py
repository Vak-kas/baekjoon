import sys;

    
    
def printList(array):
    n = len(array);
    for i in range(1, n):
        print(f"{i} --> {array[i]}")
def printVisitedAry(array):
    for i in range(1, len(array)):
        print(f"{i}", end=" ");
    
    print();
        
    for i in range(1, len(array)):
        print(f"{array[i]}", end=" ");

def makeVisitedAry(node):
    visitedAry = [-1 for _ in range(node+1)];
    return visitedAry;

def BFS(x):
    from collections import deque;
    global array;
    current = x;
    
    if len(array[current]) == 0:
        return;
    
    queue = deque();

    
    queue.append(current);
    visitedAry[current] = 0;
    count = 1
    
    while len(queue)>0:
        current = queue.popleft();
        # print(current);
        for i in array[current]:
            # print(i);
            if visitedAry[i] ==-1:
                queue.append(i);
                visitedAry[i] = visitedAry[current]+1;
        count+=1;
        
def find_node(distance):
    global visitedAry;
    ans = [];
    for i in range(1, len(visitedAry)):
        if visitedAry[i] == distance:
            ans.append(str(i));
            
    if len(ans) == 0:
        print(-1);
    else:
        print("\n".join(ans));
            
        
                
        
    
    
if __name__ == "__main__":
    node, road, distance, start = map(int, sys.stdin.readline().split());
    array = [[] for _ in range(node+1)]
    for i in range(road):
        a, b = map(int, sys.stdin.readline().split());
        array[a].append(b);
        
    visitedAry = makeVisitedAry(node);
        
        
    # printList(array);
    # print()
    BFS(start);
    # printVisitedAry(visitedAry);
    find_node(distance);
    # printVisitedAry(visitedAry);
    
        