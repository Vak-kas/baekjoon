#include <stdio.h>
#include <stdint.h>
#include <string.h>




int main(void){
    char arr[101];
    // scanf("%s", (char*)arr);
    // printf("%lu\n", sizeof(arr));
    fgets(arr, sizeof(arr), stdin);
    arr[strcspn(arr, "\n")] = '\0';

    uint32_t length = strlen(arr);


    printf("%d\n", length);

    return 0;
}