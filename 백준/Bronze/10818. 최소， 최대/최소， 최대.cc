#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
// #include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;
int main() {
    int n;
    cin >> n;

    int* arr = (int*)malloc(sizeof(int) * n);
    int max = -1000001;
    int min = 100001;
    for(int i=0;i<n;i++){
        cin >> arr[i] ;
        if(arr[i] > max){
            max = arr[i];
        }
        if(arr[i] < min){
            min = arr[i];
        }
    }

    cout << min << " " << max << endl;



}
