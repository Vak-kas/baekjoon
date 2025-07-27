#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


int rev(int n){
    int result = 0;
    int next = n;
    int remain = 0;
    while (true){
        remain = next % 10;
        // printf("remain : %d\n", remain);
        result = 10*result + remain;
        // printf("result : %d\n", result);
        next = next / 10;
        if (next == 0){
            return result;
        }
    }



}

int main(){
    int n;
    while (true){
        scanf("%d", &n);

        if(n==0){
            return 0;
        }

        int rev_n = rev(n);
        // printf("%d\n", rev_n);
        if(n==rev_n){
            printf("yes\n");
        }
        else{
            printf("no\n");
        }






    }

}