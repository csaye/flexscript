using System;

class Program
{
    static void Main()
    {
        int i = 2;
        int j = 2;
        
        while (i < 100)
        {
            bool prime = true;
            j = 2;
            
            while (j < i)
            {
                if (i % j == 0)
                {
                    prime = false;
                }
                
                j += 1;
            }
            
            if (prime)
            {
                Console.WriteLine(i);
            }
            
            i += 1;
        }
    }
}
