import sys;

n = int(sys.stdin.readline().rstrip());
lst = [];
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    lst.append(tmp);
    
lst.sort();
    



minus = list(filter(lambda x: x<-1, lst))
minus.sort(reverse=True);
plus = list(filter(lambda x: x>1, lst))

other = list(filter(lambda x: x>=-1 and x<=1, lst));

s = 0;

while len(plus)>1:
    a = plus.pop();
    b = plus.pop();
    s+=a*b;
    
if len(plus) ==1:
    s+=plus.pop();
    
while len(minus)>1:
    a = minus.pop();
    b = minus.pop();
    s+=a*b;
        



one = other.count(1);
zero = other.count(0);
minus_one = other.count(-1);

# print(minus)
# print(plus)
# print(other)
# print(one, zero, minus_one)


s+=one;
# print(s);
if len(minus) >0 and minus_one > 0:
    tmp = minus.pop();
    s+=tmp*-1;
    minus_one-=1;
    
if len(minus) > 0:
    if minus_one > 0:
        tmp = minus.pop();
        s+=tmp*-1;
        minus_one-=1;
    
    elif zero > 0:
        minus.pop();
        zero-=1;
        
    else:
        tmp = minus.pop();
        s+=tmp;
        # print(tmp)
while minus_one >=2:
    minus_one-=2;
    s+=1;
while zero>0 and minus_one > 0:
    zero-=1;
    minus_one -=1;
    
s+=-1*minus_one;

print(s)


