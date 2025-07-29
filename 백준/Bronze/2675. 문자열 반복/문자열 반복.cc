#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    int count;
    char arr[101];  // 문자열 최대 길이 100으로 가정

    for (int i = 0; i < n; i++) {
        scanf("%d %s", &count, arr);
        int length = strlen(arr);

        for (int j = 0; j < length; j++) {
            for (int q = 0; q < count; q++) {
                printf("%c", arr[j]);
            }
        }
        printf("\n");
    }

    return 0;
}
