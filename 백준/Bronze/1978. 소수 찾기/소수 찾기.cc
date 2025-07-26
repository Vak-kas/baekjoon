#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX_VALUE 1001

typedef struct{
    char n[MAX_VALUE];
} Primes;

int main(){
    int n ;
    scanf("%d", &n);
    
    int* value = (int*) malloc(sizeof(int) * n);
    for(int i=0;i<n;i++){
        scanf("%d", (value+i));
    }

    Primes prime;
    for (int i=0 ; i < MAX_VALUE ;i++){
        prime.n[i] = 1;
    }
    prime.n[0] = 0;
    prime.n[1] = 0;


    for(int i=2 ;i<MAX_VALUE ;i++){
        if(prime.n[i] == 0){
            continue;
        }
        for (int j=2; j<1000 ;j++){
            if(i*j > 1001){
                break;
            }
            prime.n[i*j] = 0;
        }
    }
    // printf("소수\n");
    // for(int i=1;i<1001;i++){
    //     if(prime.n[i] ==1){
    //         printf("%d ", i);
    //     }
    // }
    
    int count= 0;
    for (int i=0;i<n;i++){
        if (prime.n[value[i]] == 1){
            // printf("%d\n", i);
            count+=1;
        }
    }
    printf("%d\n", count);

    free(value);
}
