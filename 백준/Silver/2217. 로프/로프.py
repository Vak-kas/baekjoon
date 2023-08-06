import sys;

n = int(sys.stdin.readline().rstrip());
weight = [];
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    weight.append(tmp);
    
weight.sort(reverse=True);

max_value = -1;

for i in range(n):
    value = weight[i]*(i+1);
    if max_value < value:
        max_value = value;
        
print(max_value);
    