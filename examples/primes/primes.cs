using System;

class Program
{
    static void Main()
    {
        for (int i = 2; i < 100; i++)
        {
            bool prime = true;
            
            for (int j = 2; j < i; j++)
            {
                if (i % j == 0)
                {
                    prime = false;
                    break;
                }
            }
            
            if (prime)
            {
                Console.WriteLine(i);
            }
        }
    }
}
