#include <iostream>
#include <stdint.h>

using namespace std;

int main(void){
    cout.precision(13);
    cout << fixed;

    double a, b;
    

    cin >> a >> b;

    double c  = a/b;

    cout << c << endl;

    return 0;
}