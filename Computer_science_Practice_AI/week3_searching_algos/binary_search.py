# TODO: Implement binary search
# Remember: binary search only works on sorted arrays!

# def binary_search(arr, target):
#     # need to breka it into two, since it is sorted we can check if its on the left or right
#     # [1,2,3,4,5] n = 5  M =  5 +1 / 2 = 3 -1 
#     # check for a case that has lenght of 1
#     if (Left <= Right):
#         return -1
    
#     Right = len(arr) -1
#     Left = 0
#     middle = len(arr) //2 
#     while (Left <= Right):
#         middle = (Left + Right) // 2
#         if (arr[middle] == target):
#             return middle
#         elif (arr[middle] < target):
#             Left = middle + 1
#         else:
#             Right = middle - 1
     
#     return -1
def binary_search(arr,target):

    return  binary_search_recursive(arr,target,0,len(arr)-1)

def binary_search_recursive(arr,target,left,right):
    mid = (left + right) // 2
    if left >= right:
        return -1
    
    if (arr[mid] == target):
        return mid
    elif (arr[mid] > target):
        return binary_search_recursive(arr,target,left,mid-1)
    else:
        return binary_search_recursive(arr,target,mid+1,right)
# Test:
nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(nums, 7))   # should be 3
print(binary_search(nums, 2))   # should be -1
