using System;

class Program
{
    static void Main()
    {
        int n = 7;
        int f = 1;
        
        while (n > 1)
        {
            f *= n;
            n -= 1;
        }
        
        Console.WriteLine(f);
    }
}
