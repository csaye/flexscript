using System;

class Program
{
    static void Main()
    {
        int i = 1;
        
        while (i <= 100)
        {
            string output = "";
            
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
                Console.WriteLine(i);
            }
            else
            {
                Console.WriteLine(output);
            }
            
            i += 1;
        }
    }
}
