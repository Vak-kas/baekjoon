import sys;

def fibo(n):
    zero = [1, 0]
    one = [0, 1]
    
    if n<2:
        return zero[n], one[n]
    
    else:
        for i in range(2, n+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-1] + one[i-2]);
        # print(zero)
        # print(one);
        return zero[-1], one[-1]
    

n = int(sys.stdin.readline().rstrip());

for i in range(n):
    v = int(sys.stdin.readline().rstrip());
    
    zero, one = fibo(v);
    
    print(zero, one);

    