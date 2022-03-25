#Transform the following mathematical expression into a Python program to be able to calculate the
#result for arbitrary values of a, b, c, and d defined in the source code:
#`a - (b^2 / (c - d * (a + b)))`
#Implement it in a function `calculate` where it should be returned.
#Please make sure that your solution is self-contained within the `calculate` function. In other words, only change the body of the function, not the code outside the function.


a = 1
b = 2
c = 3
d = 4

def calc():
    res = a - ((b*b) / (c - d * (a + b)))
    return res
