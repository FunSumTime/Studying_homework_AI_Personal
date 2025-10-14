# TODO: Write a function that returns the largest number in a list/array
# Example: [3, 1, 5, 2] → 5

def find_max(nums):
    # check if the list is not empty
    if(len(nums) >= 1):
        max = nums[0]
    else:
        return "List is empty"
    # go through each varable and compare to max to see if its bigger 
    # will end up with the biggest because we go through each entry and only accept if its bigger than our local max
    for i in nums:
        if i > max:
            max = i
    return max


    # could use a max heap but to keep it simple will just use a varable to keep track of the largest
    pass  # your code here

print(find_max([3, 1, 5, 2]))
print(find_max([-10, 0, 4, 9, 2]))
