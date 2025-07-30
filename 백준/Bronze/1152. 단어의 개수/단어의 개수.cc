#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
// #include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;
int main() {
    string str ;
    getline(cin, str);
    // cout << str << endl;

    // int current = str.find(" ");
    int flag = 1;
    int count = 0;
    if(str[0] == ' '){
        flag-=1;
    }

    if(str[str.length() -1] == ' '){
        flag -=1;
    }
    for(int i=0;i<str.length() ;i++){
        if(str[i] == ' '){
            count+=1;
        }

    

    }

    cout << count + flag<< endl;


}
