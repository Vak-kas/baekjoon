def prime():
    global n, a;
    
    for i in range(2, int(len(a)**0.5)+1):
        if a[i] == 0:
            continue;
        else:
            for j in range(i+i, len(a), i):
                a[j] = 0;
    # print(a)
    primes = list(filter(lambda x : x>0, a));
    # ans = []
    for i in primes:
        tmp = str(i);
        # print(tmp, end=" ")
        if tmp == tmp[::-1]:
            if i>=n:
                print(i);
                break;
    #         ans.append(i);
            
    # print(ans)
    
    
    
    
import sys;
n = int(sys.stdin.readline().rstrip());
limit = 10000000
a = [ i for i in range(limit+1)];
a[0] = 0;
a[1] = 0;
prime()
