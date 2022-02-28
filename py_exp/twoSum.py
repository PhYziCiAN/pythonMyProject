
def twoSum1 (nums1, k):
    index = 0
    while index < len(nums1)-1:
        if (nums1[index] + nums1[index+1]) == k:
            return nums1[index], nums1[index+1]
        index +=1
    else:
        return 0 
nums1 = [-3,0,1,3,4]    
print(twoSum1(nums1,-3))

def twoSum2 (nums2, k):
    index = 0
    l = index + 1
    r = len(nums2) - 1
    while index < len(nums2)-1 and l<=r:
        numberToFind = k - nums2[index]
        mid = int((r - l)/2)
        if (nums2[mid] == numberToFind):
            return nums2[index], nums2[mid], index, mid
        elif (numberToFind < nums2[mid]):
            r = mid - 1
        else:
            l = mid + 1
        index +=1
    return 0
nums2 = [-3,0,1,3,4,7,9]   
print(twoSum2(nums2,7))