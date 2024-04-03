'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

#Test Case 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

#Test Case 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

#Test Case 3
Input: nums = [3,3], target = 6
Output: [0,1]

'''

nums = [3,3]
target = 6
output = []

def my_func():
    for i in range(len(nums)):
        for j in range(len(nums)):
            rem = target - nums[i]
            if j == i:
                continue
            if nums[i] + nums[j] == target:
                return [i,j]
            
output = my_func()
print("output", output)
