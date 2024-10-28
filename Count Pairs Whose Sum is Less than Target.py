nums = [-1,1,2,3,1]
target = 2
sum = 0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if j>i and i>=0 and nums[i] + nums[j] < target:
            sum += 1
print(sum) 