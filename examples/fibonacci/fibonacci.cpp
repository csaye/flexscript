#include <iostream>

int main()
{
    int a = -1;
    int b = 1;
    int i = 0;
    
    while (i < 10)
    {
        int c = a + b;
        a = b;
        b = c;
        std::cout << c << std::endl;
        i += 1;
    }
}
