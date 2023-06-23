import sys;

n = int(sys.stdin.readline().rstrip());
string = sys.stdin.readline().rstrip();

degree = 0;
value = 0;
M = 1234567891;
for i in string:
    a = ord(i)-96;
    value += 31**degree * a;
    degree+=1;
    
value %=M;
    
print(value);

    
    
    
