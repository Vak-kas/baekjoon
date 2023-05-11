import sys;

n, m = map(int, sys.stdin.readline().split());

array = list(map(int, sys.stdin.readline().split()));
ans = -1;

max_value = -1;
for i in range(len(array)):
    a = array[i];
    
    for j in range(i+1, len(array)):
        b = array[j];
        
        for k in range(j+1, len(array)):
            c = array[k];
            
            s = a+b+c;
            
            if s<=m and max_value<s:
                max_value = s;
                
print(max_value);
            
    