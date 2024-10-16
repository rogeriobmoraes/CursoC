nums = []

for i in range(3):
    nums.append(int(input("What's n: ")))


for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] < nums[j]):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

resultado = ', '.join(map(str, nums))
print(resultado)



