def printList(pos, important):
    num = len(important);
    ans = []
    from collections import deque;
    
    queue = deque();
    
    for i in range(num):
        queue.append((i, important[i]));
        
    while queue:
        flag = False;
        for i in range(len(queue)-1):
            if queue[0][1] < queue[i+1][1]:
                flag = True;
                break;
                
        if flag:
            tmp = queue.popleft();
            queue.append(tmp);
            # print(queue);
            
        else:
            tmp = queue.popleft();
            ans.append(tmp);
            
                
    return ans;
    



import sys;

n = int(sys.stdin.readline().rstrip());

for i in range(n):
    num, pos = map(int, sys.stdin.readline().split());
    #num -> 문서의 개수
    #pos -> queue에서 몇 번째에 놓여있는가
    
    important = list(map(int, sys.stdin.readline().split()));
    want = important[pos]
    
    ans = printList(pos, important);
    
    count = 1;
    # print(ans);
    
    
    for i in ans:
        if i[0] == pos:
            print(count);
        else:
            count+=1;
            
    
    