import sys

# 인접리스트 생성
def makeList(n):
    lst = [[] for _ in range(n+1)]
    for i in range(n-1):
        tmp = list(map(int, sys.stdin.readline().split()))
        lst[tmp[0]].append(tmp[1])
        lst[tmp[1]].append(tmp[0])
    return lst

# 인접리스트 출력
def printList(lst):
    for i in range(1, n+1):
        print(f"{i} --> ", lst[i])
        


# 인접리스트 1부터 돌면서 훑으면서 부모 노드 계산하기
def DFS(i):
    global visitedAry, edgeList;
    
    stack = [];
    stack.append(i);
    visitedAry[i] = True;
    
    while len(stack)>0:
        tmp = stack.pop();
        for v in edgeList[tmp]:
            # print(v);
            if visitedAry[v]== False: 
                stack.append(v);
                visitedAry[v] = tmp;
                
        

def printAns(ans):
    for i in range(2, len(ans)):
        print(ans[i]);

n = int(sys.stdin.readline().rstrip())
edgeList = makeList(n)
# printList(edgeList)

visitedAry = [False for _ in range(n+1)];

DFS(1);


printAns(visitedAry);

