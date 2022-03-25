#A password should contain a variety of characters to make it harder
#to guess. You are part of a team that develops a new application,
#which requires passwords to satisfy the following rules:

#* Has a length of 8-16 chars.
#* Only contains the characters a-z, A-Z, digits, or the special chars "+", "-", "*", "/".
#* Must contain at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars.

#Implement a checker that decides whether a given password candidate
#is valid. The password candidate will be given to you in a variable
#`pwd`. 

#Write a program that checks whether `pwd` satisfies all rules. The validity of the password should be verified by a function called `is_valid` and your task is to complete the function.

#Please make sure that your solution is self-contained within the `is_valid` function. That is, only change the body of the function, not the code outside the function. Your function is expected to return the validity in a bool value.

#While working on this task, these utilities will make your life easier: 
#* Use [*isupper*][isupper]/[*islower*][islower] to decide whether a string is upper case or lower case (e.g., `"A".isupper()` is `True`).
#* Use [*isdigit*][isdigit] to check if it is a number (e.g., `"3".isdigit()` is `True`).
#* Use the [`in`][in_operator] operator to check whether a specific character exists in a string (e.g., `"a" in "abc"` is `True`).

pwd = "abc"


def is_valid():
    validity = True

    size = 0
    num_lower = 0
    num_upper = 0
    num_special = 0
    num_digits = 0

    allowed_special = "+-/*"
    for c in pwd:
        size += 1
        if c.isdigit():
            num_digits += 1
        elif c.islower():
            num_lower += 1
        elif c.isupper():
            num_upper += 1
        elif c in allowed_special:
            num_special += 1
        else:
            validity = False
    validity = validity and size >= 8 and size <= 16 and num_lower > 1 and num_upper > 1 and num_digits > 1 and num_special > 1
    return validity
