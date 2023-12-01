import sys;

while True:
    lst = list(map(str, sys.stdin.readline().split()))
    if lst == []:
        break;
    s = lst[0];
    t = lst[1];


    index_t = 0
    index_s = 0;
    flag = False;


    while True:
        if s[index_s] == t[index_t] :
            index_s+=1;
            index_t +=1;
        else:
            index_t +=1;

        if index_s >= len(s):
            flag = True;
            break;

        if index_t >= len(t):
            break;

    if flag :
        print("Yes");
    else:
        print("No");
    
    
    
    