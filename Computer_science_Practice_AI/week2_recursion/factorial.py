# TODO: Write a recursive factorial function.
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Remember to define your base case (n == 0 or n == 1).

def factorial(n):
    if n < 0:
        return 0
    # print("factorial called with", n)
    # factorial is numbers times by itself counting down to one
    # base case would be if n is equal to one return 1
    # because there is nothing to return once n gets lower than one
    if n == 1:
        return 1
    else:
        # have to return this so we can recurse back up the stacks
        # when the one gets returned it will times by 2 then the 2 will times by 3 and we will be returning that values all the way up back to the original call
        result =  n * factorial(n-1)
        # print("returning result", result)
        return result

print(factorial(5))  # should print 120
print(factorial(1))  # should print 1
