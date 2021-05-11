#include <iostream>

int factorial(int n)
{
    if (n < 2)
    {
        return n;
    }
    else
    {
        return n * factorial(n - 1);
    }
}

int main()
{
    int n = 7;
    int f = factorial(n);
    std::cout << f << std::endl;
}
