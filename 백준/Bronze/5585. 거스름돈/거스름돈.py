import sys;

def change_fee(a):
    count =0;
    
    if a//500>0:
        count+=a//500;
        # print(f"500 : {500//a});
        a%=500;
        
        
    if a//100>0:
        count+=a//100;
      # print(f"100 : {100//a});
        a%=100;
    
    if a//50>0:
        count+=a//50;
        # print(f"50 : {50//a});
        a%=50;
    if a//10>0:
        count+=a//10;
      # print(f"10 : {10//a});
        a%=10;
            
    if a//5>0:
        count+=a//5;
        # print(f"5 : {5//a});
        a%=5;
    if a//1>0:
        # print(f"1 : {1//a});
        count+=a//1;
        
    return count;


money = int(sys.stdin.readline().rstrip());

a = 1000-money;

count = change_fee(a);

print(count);