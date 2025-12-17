
def insert_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        # move it up until the key is no longer bigger
        #  have j start before it
        while j >=0 and arr[j] > key:
