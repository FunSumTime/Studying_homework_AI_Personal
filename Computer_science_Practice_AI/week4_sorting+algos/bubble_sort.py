# repeadlty step through the list and bring the bigest item to the end

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # start at 0 and go up to the end
        for j in range(0,n -1 -i):
            # if n = 3 then n -1 -0 would be 2 so 0-1 would be the index of j
            # and the last index would be 2 wich would be j + 1
            if arr[j] > arr[j+1 ]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    
    return arr

nums = [5, 1, 4, 2, 8]

print(bubble_sort(nums))
# range will go up to 4 and start at 0 and be 5 counts
for i in range(5):
    print(i)
    



