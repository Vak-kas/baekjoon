import sys;
s = int(sys.stdin.readline().rstrip())
if s==1:
    print(1);
else:
    print(round(-1+(1+8*s)**0.5/2))