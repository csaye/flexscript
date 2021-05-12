#include <iostream>

int main()
{
    int unset[] = { 1, 2, 3 };
    int array[] = { 1, 2, 3 };
    array[1] = 0;
    std::cout << array[1] << std::endl;
}
