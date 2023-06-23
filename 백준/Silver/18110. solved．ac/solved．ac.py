import sys;

def findRange(k):
    a = k;
    b = int(k);
    scope = 0;
    if a-b >=0.5:
        scope = b+1;
    else:
        scope = b;
        
    return scope;
    

#의견의 개수
n = int(sys.stdin.readline().rstrip());

#난이도
difficulty=[];

#난이도 리스트 작성
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    difficulty.append(tmp);

#오름차순 정렬
difficulty.sort();
    
#범위 계산
scope = findRange(n*0.15);

if n ==0:
    print(0);
else:
    avg = sum(difficulty[scope:n-scope])/(n-2*scope);
    # print(avg);
    avg = findRange(avg)
    
    print(avg);

    

