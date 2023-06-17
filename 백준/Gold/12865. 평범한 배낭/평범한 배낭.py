def grid(row, col, weight, value):
    array = [[0 for _ in range(col+1)] for _ in range(row+1)];

    for row in range(1, row+1):
        for col in range(1, col+1):
            if col < weight[row]:
                array[row][col] = array[row-1][col];
            else:
                value1 = array[row-1][col];
                value2 = value[row] + array[row-1][col-weight[row]]
                #print(f"{row} {col} : {value1}, {value2}");
                
                array[row][col] = max(value1, value2);
                #print(array[row][col])
                
                
    return array
            
def printArray(array):
    global n, k;
    for i in range(1, n+1):
        for j in range(1, k+1):
            print(array[i][j], end="\t");
        print();
            
            

import sys;
n, k = map(int, sys.stdin.readline().split());

weight = [0];
value = [0];
for i in range(n):
    a, b = map(int, sys.stdin.readline().split());
    weight.append(a);
    value.append(b);
    
arr = grid(n, k, weight, value);
#printArray(arr);
print(arr[n][k])
    

    




