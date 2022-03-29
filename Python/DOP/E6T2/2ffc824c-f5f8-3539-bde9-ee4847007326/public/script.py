#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def preprocess(records):
    first_line = records[0]
    final_list = []
    invalid_set = ["", "undefined", "Undefined", "unknown", "Unknown"]
    survived_set = ["yes", "t", "Yes", "survived", "Survived", "true", "T", "Alive", "True"]
    dead_set = ["no", "false", "F", "dead", "Dead", "No", "f", "False", "Survived=dead"]
    male_set = ["male", "Male", "m", "M"]
    female_set = ["female", "f", "F", "Female"]

    for p in records[1:]:
        if p[0] in invalid_set:
            continue
        elif p[0] in survived_set:
            s = True
        elif p[0] in dead_set:
            s = False
        else:
            print(p[0])
        if p[1] in invalid_set:
            continue
        elif int(p[1]) == 1 or int(p[1]) == 2 or int(p[1]) == 3:
            pc = int(p[1])
        else:
            continue
        if p[2] in invalid_set:
            continue
        else:
            name = p[2]
        if p[3] in invalid_set:
            continue
        elif p[3] in male_set:
            g = "male"
        elif p[3] in female_set:
            g = "female"
        else:
            print(p[3])
        if p[4] in invalid_set or float(p[4]) <= 0 or float(p[4]) > 100:
            continue
        else:
            age = float(p[4])
        if p[5] in invalid_set:
            f = float(25)
        else:
            f = float(p[5])

        final_list.append((s, pc, name, g, age, f))

    filtered_list = (first_line, final_list)
    return filtered_list



# The following part calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the function that you have written in Task 1.
# The following example is not complete.

titanic = [
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
    ('no', '3', 'Braund Ms. Maria', 'Female', '22', ''),
    ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
    ('', '3', 'Vander Planke Miss. Augusta Maria', 'female', '', ''),
    ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')
    # ...
]

print(preprocess(titanic))
