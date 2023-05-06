# import sys

# #인접리스트 생성
# def makeList(n):
    
#     lst = [[] for _ in range(n+1)];
    
#     for i in range(n-1):
#         tmp = list(map(int, sys.stdin.readline().split()));
#         lst[tmp[0]].append(tmp[1]);
#         lst[tmp[1]].append(tmp[0]);
#     return lst;

# #인접리스트 출력
# def printList(lst):
#     for i in range(1, n+1):
#         print(f"{i} --> ", lst[i]);
        


# #인접리스트 1부터 돌면서 훑으면서 부모 노드 계산하기
# def DFS(lst, start):
    
#     ans = [0 for _ in range(len(lst))]
#     stack = []
#     visitedAry = []
    
#     stack.append(start)
#     visitedAry.append(start);
#     current = start;
#     index = 0;
    
#     while True:
#         # print(f"현재 위치 : {current} {index}")

#         try:
#             next = lst[current][index];
#             if next in visitedAry:
#                 index+=1;
#             else:
#                 ans[next] = current;
#                 current = next;
#                 stack.append(current);
#                 visitedAry.append(current);
#                 index = 0;
#         except:
#             try:
#                 current = stack.pop();
#                 index = 0;
#             except:
#                 break;
                
#     return ans;
                
# def printAns(ans):
#     for i in ans[2:]:
#         print(i);
    
                
        


# n = int(sys.stdin.readline().rstrip());
# lst = makeList(n)
# printList(lst);


# root = 1;

# ans = DFS(lst, root);

# #답 출력하기
# printAns(ans);
    

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
def DFS(lst, start):
    ans = [0 for _ in range(len(lst))]
    stack = []
    visitedAry = []
    stack.append(start)
    visitedAry.append(start)
    current = start
    index = 0
    while True:
        try:
            next = lst[current][index]
            if next in visitedAry:
                index += 1
            else:
                ans[next] = current
                current = next
                stack.append(current)
                visitedAry.append(current)
                index = 0
        except:
            try:
                current = stack.pop()
                index = 0
            except:
                break
    return ans

def printAns(ans):
    for i in range(2, len(ans)):
        print(ans[i])

n = int(sys.stdin.readline().rstrip())
lst = makeList(n)
# printList(lst)
root = 1
ans = DFS(lst, root)
printAns(ans)
