using System;

class Program
{
    static void Main()
    {
        int[] unset;
        unset = new int[] { 1, 2, 3 };
        int[] array = { 1, 2, 3 };
        array[1] = 0;
        Console.WriteLine(array[1]);
    }
}
