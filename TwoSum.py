def twoSum(size, nums, target):
    for i in range(size):
        for j in range(i+1, size): 
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]


size = int(input("Size of the array: "))
nums = []
for i in range(size):
    element = int(input("Enter Array"))
    nums.append(element)
print("The array is:", nums)

target = int(input("Enter target: "))

result = twoSum(size, nums, target)
print("result", result)
