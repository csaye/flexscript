using System;

class Program
{
    static void Doublearray(int[] array, int size)
    {
        for (int i = 0; i < size; i++)
        {
            int newvalue = array[i] * 2;
            array[i] = newvalue;
        }
    }
    
    static void Main()
    {
        int[] nums = { 1, 2, 3 };
        int size = nums.Length;
        Doublearray(nums, size);
        
        foreach (int num in nums)
        {
            Console.WriteLine(num);
        }
    }
}
