import sys;

def binary_search(s):
    global lan, n;
    start = 1;
    end = s+1;
    before = 0;
    
    while start<=end:
        mid = (start+end)//2;

        
        count = 0;
        for i in lan:
            count+=i//mid;
        
        # print(mid, count);
            
        if count == n:
            if before <mid:
                before = mid
                start = mid+1

            
        elif count > n:
            start = mid+1;
            before = mid;
        else:
            end = mid-1;
    
    if count < n:
        mid = before;
    while True:
        tmp = mid;
        tmp+=1;
        
        count = 0;
        for i in lan:
            count+=i//tmp;
            
        if count == n:
            mid = tmp;
        else:
            break;
            
    return mid;
        
        
k, n = map(int, sys.stdin.readline().split());

lan = [];

for i in range(k):
    tmp = int(sys.stdin.readline().rstrip());
    lan.append(tmp);
    
s = sum(lan);

a = binary_search(s);

print(a);
