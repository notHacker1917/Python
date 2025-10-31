def checkMax(arr):
    max_val = arr[0]  
    for n in arr:    
        if n > max_val:
            max_val = n
    print("Maximum value:", max_val)


size = int(input("Size of the array: "))
nums = []
for i in range(size):
    element = int(input("Enter array element: "))
    nums.append(element)
checkMax(nums)
