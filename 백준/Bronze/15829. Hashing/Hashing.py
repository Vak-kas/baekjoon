import sys;

n = int(sys.stdin.readline().rstrip());
string = sys.stdin.readline().rstrip();

degree = 0;
value = 0;
for i in string:
    a = ord(i)-96;
    value += 31**degree * a;
    degree+=1;
    
print(value);

    
    
    