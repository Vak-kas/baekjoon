#include <iostream>

using namespace std;
int main()
{
    int a, b;
    std::cin >> a ;
    std::cin >> b;
    if(a > b)
    {
        std::cout << ">" << std::endl;
    }
    else if(a < b)
    {
        cout << "<" << endl;
    }
    else
    {
        cout << "==" << endl;
    }
    return 0;
}