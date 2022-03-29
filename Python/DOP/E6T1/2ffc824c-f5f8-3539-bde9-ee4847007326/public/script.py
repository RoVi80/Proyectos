#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def read_csv(path):
    res_lst = []
    with open(records) as f:
        for l in f:
            if l == "\n":
                pass
            else: 
                str_l = str(l)
                str_l_stripped = str_l.strip()
                str_l_splitted = str_l_stripped.split(",")
                line_as_tuple = tuple(str_l_splitted)
                res_lst.append(line_as_tuple)


    alive = ["Survived", "survived", "Yes", "yes", "T", "t", "Alive", "alive", "True", "true"]
    dead = ["Dead", "dead", "No", "no", "F", "f", "False", "false", "Survived=dead"]
    male = ["Male", "male", "M", "m"]
    female = ["Female", "female", "F", "f"]
    age_value = ["", "undefined", "unknown", "Undefined"]
    fare_value = ["", "undefined"]

    headers = res_lst[0]
    lst_of_entries = res_lst[1:]

    lst_t = []
    tmp_lst = []
    line_lst = []
    final_lst = []

    for t in lst_of_entries:
        lst_t_tmp = list(t)
        lst_t.append(lst_t_tmp)

    
    for i in lst_t:
        for k in range(len(i)):
            
            if len(i) < 5 or i[4] == "":
                tmp_lst = []
                break

            if k == 0:
                if i[k] in alive:
                    tmp_lst.append(True)
                    #i[0] = True
                elif i[k] in dead:
                    tmp_lst.append(False)
                    #i[0] = False
                else:
                    tmp_lst = []
                    #del(i)
                    break
    
            if k == 1:
                pclass = int(i[k])
                if pclass < 1 or pclass > 3:
                    tmp_lst = []
                    break
                else:
                    tmp_lst.append(pclass)
            
            if k == 2:
                tmp_lst.append(i[k])
            
            if k == 3: 
                if i[k] in male: 
                    tmp_lst.append("male")
                elif i[k] in female:
                    tmp_lst.append("female")
                else:
                    tmp_lst = []
                    break
            
            if k == 4:
                if i[k] not in age_value: 
                    age = float(i[k])
                    if age < 0.0 or age > 100.0:
                        tmp_lst = []
                        break
                    else: 
                        tmp_lst.append(age)
            
            if k == 5:
                if i[k] not in fare_value:
                    if i[k]:
                        tmp_lst.append(float(i[k]))
                    else:
                        tmp_lst.append(25.0)
                    tmp_lst = []
                    break
        if tmp_lst:
            line_lst.append(tuple(tmp_lst))
            tmp_lst = []
    final_lst.append(line_lst)

    print(final_lst)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(read_csv("public/example.csv"))
