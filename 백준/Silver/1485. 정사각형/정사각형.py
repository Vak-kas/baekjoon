import sys;

t = int(sys.stdin.readline().rstrip());
for _ in range(t):
    lst = [0]*4;
    for i in range(4):
        lst[i] = list(map(int, sys.stdin.readline().split()));
        
    distance = [];
    for i in range(4):
        for j in range(i+1, 4):
            a = lst[i];
            b = lst[j];
            
            dis = (a[0]-b[0])**2 + (a[1]-b[1])**2;
            dis = dis**0.5;
            
            distance.append(dis);
            
            
    distance.sort();
    
    if distance[0] == distance[1] == distance[2] == distance[3]:
        if distance[4] == distance[5]:
            print(1);
        else:
            print(0);
    else:
        print(0);
        
        