import sys;

n = int(sys.stdin.readline().rstrip());
i = 0;
end = 0;
while i*(i+1)//2 < n :
    i+=1;
    end+=i;
    
start = end - i+1;

    
if i%2 == 0:
    child = 1;
    parent = i;
    while start < n:
        start+=1;
        parent -=1;
        child +=1;
    
else:
    child = i;
    parent = 1;
    while start < n:
        start+=1;
        parent +=1;
        child -=1;
        
        
print(f"{child}/{parent}")
    

    
    

    
    
    
    