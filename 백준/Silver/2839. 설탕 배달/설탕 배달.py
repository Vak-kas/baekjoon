N = int(input());

x = N//5;
y = N%5;


while True:
    if y%3 !=0:
        x-=1;
        y+=5;
        if x<0:
            print(-1);
            break;
    else:
        k = y//3;
        print(x+k);
        break;

        

        
