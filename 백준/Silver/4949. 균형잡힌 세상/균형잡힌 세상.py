import sys;

def balance(string):
    flag =True;
    n = len(string);
    stack = [];
    for i in range(n):
        try:
            if string[i] == "(":
                stack.append(string[i]);
            elif string[i] == "[":
                stack.append(string[i]);
            elif string[i] == "]":
                tmp = stack.pop();
                if tmp =="[":
                    pass;
                else:
                    flag = False;
                    return flag;

            elif string[i] == ")":
                tmp = stack.pop();
                if tmp == "(":
                    pass;
                else:
                    flag = False;
                    return flag;
        except:
            flag = False;
            return flag
    if len(stack) == 0:
        return flag;
    else:
        flag = False;
        return flag;
        

while True:
    string = sys.stdin.readline().rstrip();
    
    if string == ".":
        break;
        
    a = balance(string);
    
    if a:
        print("yes");
    else:
        print("no");
    
    