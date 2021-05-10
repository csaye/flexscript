#include <iostream>

int main()
{
    int i = 1;
    
    while (i <= 100)
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
        
        i += 1;
    }
}
