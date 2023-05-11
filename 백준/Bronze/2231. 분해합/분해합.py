import sys;

a = int(sys.stdin.readline().rstrip());
str_a = str(a);
# array = [int(i) for i in tmp];
# print(sum(array));
n = len(str_a)
if n<3:
    min_value = a;
else:
    min_value = 9*(n);

start = a-min_value;
# print(start);
ans = 0;
for i in range(start, a):
    t = str(i);
    array = [int(i) for i in t]
    s = sum(array);
    # print(i, s, start+s);

    
    if i+s == a:
        ans = i
        break;
        
print(ans);
        
