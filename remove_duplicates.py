#solution works in my ide but fails on leet code 

nums = [0,0,1,1,1,2,2,3,3,4]
my_set = set() 

for num in nums:
    if num in my_set:
        continue 
    else:
        my_set.add(num)

nums = list(my_set)
nums.sort()

k = len(nums)
print("list:", nums)
print("list size:", k)

#solution obtained from leetcode 
j = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[j] = nums[i]
        j += 1