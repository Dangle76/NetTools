#!/usr/bin/python

def median(nums):
    nums = nums.sort()
    mid=0
    if len(nums)%2 == 0:
        mid = len(nums)/2
        return (nums[mid]+nums[mid-1])/2.0
    else:
        mid = (len(nums)-1)/2
        return nums[mid]
print median([1,3,5])
