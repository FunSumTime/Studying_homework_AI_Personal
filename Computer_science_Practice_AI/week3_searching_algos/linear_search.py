# TODO: Implement linear search
# Should return the index of the target, or -1 if not found.

def linear_search(arr, target):
    # to see what they look like
    # print(arr)
    # print(target)
    index_at = -1
    # we do in as that is how pythons for loops work.
    #they work on iterable objects: An iterable is an object capable of returning its members one at a time
    # so this goes one by one in the object like doing pointers going down a list
    for i in range(len(arr)):
        # going through each element and checking the value
        # can use i for the return and assume only one instance of the object or we just get the first one in the order
        if (arr[i] == target):
            # we have found the target
            # can return here or set a varable and return
            index_at = i
            break
            # return i
    return index_at
    # testing to see if i need to do len(arr) -1
    # print()
    # print(len(arr))

# Test:
print(linear_search([5, 3, 7, 2, 8], 7))  # should be 2
print(linear_search([1, 4, 6, 9], 2))    # should be -1
