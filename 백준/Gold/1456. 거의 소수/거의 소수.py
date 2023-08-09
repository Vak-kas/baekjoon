import sys;
def prime():
    global a, b
    limit = 10**7
    
    primes = [i for i in range(limit+1)];
    primes[0] = 0;
    primes[1] = 0;
    
    for i in range(2, int(len(primes)**0.5) +1):
        if primes[i] == 0:
            continue
        for j in range(i+i, len(primes), i):
            primes[j] = 0;
            
    count = 0;
    
    for i in range(2, 10**7 +1):
        if primes[i] !=0:
            tmp = primes[i];
            tmp *=primes[i];
            
            while tmp <= b:
                if tmp>=a:
                    count+=1;
                tmp*=primes[i];
                
    return count
    



a, b = map(int, sys.stdin.readline().split());
print(prime());






