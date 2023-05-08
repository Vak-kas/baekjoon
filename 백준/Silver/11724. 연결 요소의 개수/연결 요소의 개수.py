import sys;



def printEdgeList(edgeList):
    for i in range(1, len(edgeList)):
        print(f"{i} --> {edgeList[i]}")
        
def printVisitedAry(visitedAry):
    for i in range(1, len(visitedAry)):
        print(f"{visitedAry[i]}", end= " ");
    print();
                   
        

def DFS(i):
    stack = [];
    global visitedAry, edgeList;
    
    stack.append(i);
    # print(i);
    visitedAry[i] = True;
    
    while len(stack)>0:
        n = len(edgeList[i]);
        tmp = stack.pop();
        for j in edgeList[tmp]:
            if not visitedAry[j]:
                stack.append(j);
                visitedAry[j] = True;
                # print(j)
        # print(visitedAry)
    # print("count!", i);
            
    


node, edge = map(int, sys.stdin.readline().split());
edgeList = [[] for _ in range(node+1)];
for i in range(edge):
    a, b = map(int, sys.stdin.readline().split());
    edgeList[a].append(b);
    edgeList[b].append(a);
                  
visitedAry = [False for _ in range(node+1)]

count = 0;
for i in range(1, node+1):
    if visitedAry[i] == False:
        # print(i)
        count+=1;
        DFS(i);
        
print(count);
    
# printEdgeList(edgeList);
# printVisitedAry(visitedAry);






