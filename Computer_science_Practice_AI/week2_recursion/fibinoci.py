# TODO: Write a recursive Fibonacci function.
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
import sys
print(sys.getrecursionlimit())

def fibonacci(n):
    # print("calling with ", n)
    # base cases as 0 and 1 would just be one or zero 
    if n == 0:
        return 0
    if n == 1:
        return 1
    # will just do n-1 plus n-2 fibonacci
    #  which will recurse to get the fibonaci for n-1 whcih will branch off to its own thing until the tree comes back up
    result = fibonacci(n-1) + fibonacci(n-2)
    # print("result is", result)
    return result
# Test:
print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(5))  # 5
print(fibonacci(8))  # 21
