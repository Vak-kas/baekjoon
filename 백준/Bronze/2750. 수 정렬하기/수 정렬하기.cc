#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void print_arr(int* arr, int n){
    for(int i=0;i<n;i++){
        printf("%d\n" , arr[i]);
    }

}
void swap(int* a, int* b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;

}

void bubble_sort(int* arr, int n){
    for (int i=0;i<n-1;i++){
        for (int j=0; j<n-1 ;j++){
            if(arr[j] > arr[j+1]){
                swap((arr+j), (arr+(j+1)));
            }
        }
        // print_arr(arr, n);
        // printf("\n");
    }



}

int main(){
    int n;
    scanf("%d", &n);
    int* arr = (int*) malloc (sizeof(int) * n);
    for(int i= 0 ;i<n;i++){
        scanf("%d", &arr[i]);
    }
    bubble_sort(arr, n); 

    // printf("\n");
    print_arr(arr, n);

}