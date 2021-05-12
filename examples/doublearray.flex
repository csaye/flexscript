void doublearray(int[] array, int size)
{
    for (int i = 0; i < size; i++)
    {
        int newvalue = array[i] * 2;
        array[i] = newvalue;
    }
}

#_MAIN
int[] nums = { 1, 2, 3 };
int size = alen(nums);
doublearray(nums, size);

foreach (int num in nums)
{
    print(num);
}
