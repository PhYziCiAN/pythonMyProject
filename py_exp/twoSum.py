
def twoSum (nums, k):
    index = 0
    while index < len(nums)-1:
        if (nums[index] + nums[index+1]) == k:
            return nums[index], nums[index+1]
        index +=1
    else:
        return 0 
nums = [-3,0,1,3,4]    
print(twoSum(nums,7))