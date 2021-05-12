function doublearray(array, size)
{
    for (var i = 0; i < size; i++)
    {
        var newvalue = array[i] * 2;
        array[i] = newvalue;
    }
}

var nums = [1, 2, 3];
var size = nums.length;
doublearray(nums, size);

for (var num of nums)
{
    console.log(num);
}
