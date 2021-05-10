#include <iostream>

int main()
{
    for (int i = 1; i < 101; i++)
    {
        std::string output = "";
        
        if (i % 3 == 0)
        {
            output += "Fizz";
        }
        if (i % 5 == 0)
        {
            output += "Buzz";
        }
        
        if (output == "")
        {
            std::cout << i << std::endl;
        }
        else
        {
            std::cout << output << std::endl;
        }
    }
}
