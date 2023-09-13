a = [];
b = [];
for i in range(1, 31):
    a.append(i);
    
for j in range(28):
    k = int(input());
    b.append(k)
        
    
m = set(a);
n = set(b);

l = list(m-n);

l.sort();

print(l[0]);
print(l[1]);


    