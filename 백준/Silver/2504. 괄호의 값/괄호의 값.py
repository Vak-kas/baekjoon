import sys;


def correct(s):
    stack = [];
    try:
        for i in s:
            if i=="(":
                stack.append(i);
            elif i=="[":
                stack.append(i);
            elif i==")":
                q = stack.pop();
                if q!="(":
                    return False;
            else:
                q = stack.pop();
                if q!="[":
                    return False;
    except:
        return False
            
    if len(stack) == 0:
        return True;
    
    return False;

s = input()

if correct(s):
    sik = " "

    for i in range(len(s)-1):
        if s[i]=="(":
            sik +="2*("
            # print(sik)
        elif s[i]==")":
            if s[i+1] =="(" or s[i+1] == "[":
                sik += "1)+"
            else:
                sik+="1)*"
        elif s[i]=="[":
            sik +="3*("
        elif s[i]=="]":
            if s[i+1] =="(" or s[i+1] == "[":
                sik += "1)+"
            else:
                sik+="1)*"
                
    sik+="1)";
    

    try:
        # print(sik)
        print(eval(sik))
    except:
        print(0);
    
    

else:
    print(0);

