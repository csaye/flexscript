using System;

class Program
{
    static void Main()
    {
        for (int i = 1; i < 101; i++)
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
        }
    }
}
