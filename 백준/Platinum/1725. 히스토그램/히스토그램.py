import sys;

n = int(sys.stdin.readline().rstrip());
lst = [];

for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    lst.append(tmp);
lst.append(0);
# print(lst);
stack = [];
left = 0;
stack.append((left, lst[0]));
result = 0;

for i in range(1, n+1):
    left = i;
    while stack and stack[-1][1] > lst[i]:
        left, h = stack.pop();
        result = max(result, (i-left)*h);
    stack.append((left, lst[i]))
    
print(result);