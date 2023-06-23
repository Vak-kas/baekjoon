import sys;

def sansul(lst):
    if len(lst)==1:
        return lst[0];
    s = sum(lst);
    l = len(lst);
    
    return round(s/l);

def middle(lst):
    if len(lst)==1:
        return lst[0];
    center = len(lst)//2;
    return lst[center]
n = int(sys.stdin.readline().rstrip());

def many(lst):
    if len(lst) == 1:
        return lst[0]
    dic={};
    for i in lst:
        if i not in dic:
            dic[i] = 1;
        else:
            dic[i] +=1;
            
    d1 = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    if d1[0][1] == d1[1][1]:
        return d1[1][0]
    return d1[0][0]


def scope(lst):
    if len(lst)==1:
        return 0;
    else:
        return lst[-1]-lst[0]

lst = [0]*n;

for i in range(n):
    tmp= int(sys.stdin.readline().rstrip());
    lst[i] = tmp;
    

lst.sort();

print(sansul(lst));
print(middle(lst));
print(many(lst));
print(scope(lst));

