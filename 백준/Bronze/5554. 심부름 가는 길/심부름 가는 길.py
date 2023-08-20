import sys;

a = int(sys.stdin.readline().rstrip());
b = int(sys.stdin.readline().rstrip());
c = int(sys.stdin.readline().rstrip());
d = int(sys.stdin.readline().rstrip());

total = a+b+c+d;

hour = total//60;
minite = total%60;
print(hour)
print(minite);