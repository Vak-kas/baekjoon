#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>



int main(void){
    int n ;
    scanf("%d", &n);

    int* score  = (int*)malloc(sizeof(int)*n);
    int max = -1;

    for (int i = 0 ; i<n ; i++){
        scanf("%d", (score+i));
        if (score[i] > max) {
            max = score[i];
        }
    }

    double result;
    for (int i=0;i<n;i++){
        result = result + (double)score[i];
    }
    result = result * 100 / max / n;

    printf("%.9lf\n", result);
}