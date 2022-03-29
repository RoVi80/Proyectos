#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    h_list = {}
    for i in posts:
        for word in i.split():
            if word.startswith('#') and len(word) != 1:
                if word.replace('#', '') not in h_list:
                    h_list[word.replace('#', '')] = 1
                else:
                    h_list[word.replace('#', '')] += 1

            if word.startswith('.#') and len(word) != 1:
                if word.replace('.#', '') not in h_list:
                    h_list[word.replace('.#', '')] = 1
                else:
                    h_list[word.replace('#', '')] += 1

    return (h_list)



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))