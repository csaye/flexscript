using System;

class Program
{
    static int Factorial(int n)
    {
        if (n < 2)
        {
            return n;
        }
        else
        {
            return n * Factorial(n - 1);
        }
    }
    
    static void Main()
    {
        int n = 7;
        int f = Factorial(n);
        Console.WriteLine(f);
    }
}
