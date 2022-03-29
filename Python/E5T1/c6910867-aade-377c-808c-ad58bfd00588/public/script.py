#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    mergelist = []
    if len(a) == len(b):
        l_same_len = list(zip(a, b))
        return l_same_len
    elif len(a) == 0 or len(b) == 0:
        return mergelist
    elif len(a) > len(b):
        for i in range(0, len(b)):
            a_p = a.pop(0)
            b_p = b.pop(0)
            mergelist.append((a_p, b_p))
        for i in range(0, len(a)):
            a_p = a.pop(0)
            b_tmp = b_p
            mergelist.append((a_p, b_tmp))
        return mergelist
    elif len(a) < len(b):
        for i in range(0, len(a)):
            a_p = a.pop(0)
            b_p = b.pop(0)
            mergelist.append((a_p, b_p))
        for i in range(0, len(b)):
            b_p = b.pop(0)
            a_tmp = a_p
            mergelist.append((a_tmp, b_p))
        return mergelist




# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([], [2, 3]))
