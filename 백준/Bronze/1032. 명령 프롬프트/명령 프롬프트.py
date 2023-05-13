import sys;

n = int(sys.stdin.readline().rstrip());
string = [0 for _ in range(n)];
for i in range(n):
    tmp = sys.stdin.readline().rstrip();
    string[i] = tmp;
    
l = len(string[0]);

ans = "";
for i in range(l):
    flag = True;
    standard = string[0][i];
    for j in range(n):
        if string[j][i] !=standard:
            flag = False;
            
    if flag == False:
        ans +="?";
    else: ans +=standard;
        
print(ans);
        