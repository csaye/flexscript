public class Main
{
    static void doublearray(int[] array, int size)
    {
        for (int i = 0; i < size; i++)
        {
            int newvalue = array[i] * 2;
            array[i] = newvalue;
        }
    }
    
    public static void main(String[] args)
    {
        int[] nums = { 1, 2, 3 };
        int size = nums.length;
        doublearray(nums, size);
        
        for (int num : nums)
        {
            System.out.println(num);
        }
    }
}
