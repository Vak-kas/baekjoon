import sys;

def whiteStart():
    lst = [["W" for _ in range(8)] for _ in range(8)];
    
    for i in range(8):
        if i%2==0:
            for j in range(1, 8, 2):
                lst[i][j] = "B";
        else:
            for j in range(0, 8, 2):
                lst[i][j] = "B";
                
    return lst;

def blackStart():
    lst = [["B" for _ in range(8)] for _ in range(8)];
    
    for i in range(8):
        if i%2==0:
            for j in range(1, 8, 2):
                lst[i][j] = "W";
        else:
            for j in range(0, 8, 2):
                lst[i][j] = "W";
    return lst
    

def printLst(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end=" ");
        print();
        
def makeChess():
    global row, col;
    
    lst = [[None for _ in range(col)] for _ in range(row)];
    
    for i in range(row):
        tmp = sys.stdin.readline().rstrip();
        for j in range(len(tmp)):
            lst[i][j] = tmp[j];
            
    return lst;

def makeTmp(i,j):
    global chess;
    tmp = []
    for p in range(i, i+8):
        tmp.append(chess[p][j:j+8]);
    return tmp
            
    
            
    

def compareLst(tmp, lst):
    count = 0;
    for i in range(8):
        for j in range(8):
            if tmp[i][j] !=lst[i][j]:
                count+=1;
            
    return count;
            
            
        


row, col = map(int, sys.stdin.readline().split());

chess = makeChess();

minChange = 9999;
lst = []
for i in range(row):
    for j in range(col):
        if ((i+8) > row) or ((j+8) > col):
            break;
            
        tmp = makeTmp(i, j);
        lst1 = whiteStart();
        lst2 = blackStart();
        count1 = compareLst(tmp, lst1);
        count2 = compareLst(tmp, lst2);
        
        if count1>count2:
            count = count2;
        else:
            count = count1;
        
        if minChange > count:
            minChange = count;
            
printLst(lst);
print(minChange);
            
            
        



