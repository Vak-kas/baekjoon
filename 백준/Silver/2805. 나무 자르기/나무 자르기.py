
import sys

def cut_tree(max_height):
    global m, wood_height;
    
    start = 0;
    end = max_height;
    mh = -1
    
    while start<=end:
        mid = (start+end)//2;
        # print(f"mid : {mid}")
        tree = 0;
        for i in wood_height:
            if i-mid>0:
                tree+=(i-mid)
        
        if tree < m:
            end = mid-1;
        elif tree == m:
            return mid;
        else:
            start = mid+1
            if mid > mh:
                mh = mid;
    if mh == -1:
        return 0;
    return mh
    
n, m = map(int, sys.stdin.readline().split());
wood_height = list(map(int, sys.stdin.readline().split()))
max_height = max(wood_height);
print(cut_tree(max_height))

    
