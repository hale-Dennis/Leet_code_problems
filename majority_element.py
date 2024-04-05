'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

def majorityElement(nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]

majority = majorityElement([1,3,1,2,3,1,1])
print(majority)