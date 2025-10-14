# TODO: Write a function that takes a string and returns it reversed
# Example: "hello" → "olleh"

def reverse_string(s):
    ans = ""
    # we can write a for loop that will go backwards or maybe we could use the [] operator to do some things in python
    # for this i need to figure out which things do what at each space in the []
    # range works the same as the [] operator where it has three places start end and step counter
    # i have to do len(s) -1 because on hello that would give 5 and that would not be a valid index as stirngs, lists and stuff start at zero index not one

    for i in range(len(s)  -1,-1,-1):
        ans += s[i]
        
    # print(ans)
    # [_,_,_] it has three places
    # first is the start index
    # second is the ending index
    # third is the step or how much it increments
    # so if i leave both blank and do a negetive step that would make it step backwards at a rate of 1
    return s[::-1]  # your code here

# Test it:
b = reverse_string("hello")
print(b == "olleh")
print(reverse_string("hello"))
print(reverse_string("CS rocks!"))
