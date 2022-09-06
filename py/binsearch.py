# binsearch.py
# Adam Driggers
# CSCI 77800 Fall 2022
# collaborators:
# consulted:

def isSorted(nums):
    end = len(nums) - 1
    for i in range(end): 
        # print(i, num)
        if nums[i] > nums[i+1]: 
            return False
    return True

# recrusive binary search 
def binSearch(nums, target, low, high):
    tPos = -1
    mPos = int((low + high) / 2) #type cast to force integer div
   
    # exit case, value not found
    if low > high:
        return -1
    
    # target found
    if nums[mPos] == target:
        return mPos
    elif nums[mPos] > target:
        return binSearch(nums, target, low, mPos-1)
    elif nums[mPos] < target:
        return binSearch(nums, target, mPos+1, high)

    return tPos

# main
nums = [2, 4, 6, 8, 42]
print(nums)
print(isSorted(nums)) # not using here, but you can only do a binsearch on a sorted array, this will test if an array is sorted 

print(binSearch(nums, 8, 0, len(nums)-1)) # should print 3

# looking for a value not in the array, will be -1 
print(binSearch(nums, 9, 0, len(nums)-1))
 
