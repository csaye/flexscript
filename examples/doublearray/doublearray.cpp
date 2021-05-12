#include <iostream>

void doublearray(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        int newvalue = array[i] * 2;
        array[i] = newvalue;
    }
}

int main()
{
    int nums[] = { 1, 2, 3 };
    int size = std::size(nums);
    doublearray(nums, size);
    
    for (int num : nums)
    {
        std::cout << num << std::endl;
    }
}
