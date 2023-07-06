import sys
height = [];
for i in range(9):
    tmp = int(sys.stdin.readline().rstrip());
    height.append(tmp);
no = []
s = sum(height);
isfind = False
for i in range(len(height)-1):
    for j in range(i+1, len(height)):
        a = height[i];
        b = height[j];
        if s-a-b == 100:
            no.append(a);
            no.append(b);
            isfind = True;
            # print(height)
            break;
            
    if isfind :
        break;
        
height.sort();
for i in height:
    if i not in no:
        print(i);
            