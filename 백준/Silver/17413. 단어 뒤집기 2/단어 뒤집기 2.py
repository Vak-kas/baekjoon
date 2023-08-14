import sys;

n = sys.stdin.readline().rstrip();
n+= " "
idx = 0;
flag = False;
word = ""
lst = []
while idx<len(n):
    if n[idx] == "<":
        if word=="":
            pass;
        else:
            lst.append(word[::-1]);
            word=""
            
        word+=n[idx];
        flag = True;
        idx+=1;
        continue;
        
    elif n[idx] == ">":
        word+=n[idx];
        flag = False;
        lst.append(word);
        word = "";
        idx+=1;
        continue;
        
    if flag == True:
        word+=n[idx];
        idx+=1
        
    else:
        if n[idx] ==" ":
            word = word[::-1];
            word+=" "
            lst.append(word);
            idx+=1;
            word=""
        else:
            word +=n[idx];
            idx+=1;
        
        
            
        
        
# print(lst)
print("".join(lst));