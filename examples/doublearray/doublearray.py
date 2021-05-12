def doublearray(array, size):
    for i in range(0, size):
        newvalue = array[i] * 2
        array[i] = newvalue

nums = [1, 2, 3]
size = len(nums)
doublearray(nums, size)

for num in nums:
    print(num)
