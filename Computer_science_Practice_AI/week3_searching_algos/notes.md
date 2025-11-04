1. Linear Search

Idea: Go through each element one by one until you find the target.

Use when: The list is unsorted.

Big-O time complexity: O(n) (worst case = look at every item).

2. Binary Search

Idea: Works only on sorted lists.

Split the list in half, decide which half to keep searching, and repeat.

Big-O time complexity: O(log n) (very fast).

## Week 3 (Linear Search)

- iterable objects are things that return things in order one by one
- using that we can loop over everything in a object and check for certain propertys
- giving us N complexity as we search N items

## Week 3 (Binary Search)

- Always update mid = (left + right) // 2 each iteration.
- Loop condition is left <= right, not left != right.
- If arr[mid] < target → search right side (left = mid + 1).
- If arr[mid] > target → search left side (right = mid - 1).
- Integer division (//) avoids fractions when finding middle.
