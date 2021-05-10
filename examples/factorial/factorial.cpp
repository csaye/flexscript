#include <iostream>

int main()
{
    int n = 7;
    int f = 1;
    
    while (n > 1)
    {
        f *= n;
        n -= 1;
    }
    
    std::cout << f << std::endl;
}
