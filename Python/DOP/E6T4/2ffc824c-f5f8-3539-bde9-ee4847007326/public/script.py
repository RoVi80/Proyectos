#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def visualize(records):
    total_p = 0
    fc = 0
    sc = 0
    tc = 0
    fc_alive = 0
    sc_alive = 0
    tc_alive  = 0

    for i in records[1]:
        i_list = list(i)
        if i_list[1] == 1:
            fc += 1
            if i_list[0] == True:
                fc_alive += 1
        if i_list[1] == 2:
            sc += 1
            if i_list[0] == True:
                sc_alive += 1
        if i_list[1] == 3:
            tc += 1
            if i_list[0] == True:
                tc_alive += 1

        total_p += 1
    
    percent_fc = round((float(fc)/float(total_p) * 100), 1)
    percent_sc = round((float(sc)/float(total_p) * 100), 1)
    percent_tc = round((float(tc)/float(total_p) * 100), 1)
    percent_fc_alive = round((float(fc_alive)/float(fc) * 100), 1)
    percent_sc_alive = round((float(sc_alive)/float(sc) * 100), 1)
    percent_tc_alive = round((float(tc_alive)/float(tc) * 100), 1)

    int_percent_f = int((round(percent_fc / 5)))
    int_percent_s = int((round(percent_sc / 5)))
    int_percent_t = int((round(percent_tc / 5)))
    int_percent_f_al = int((round(percent_fc_alive / 5)))
    int_percent_s_al = int((round(percent_sc_alive / 5)))
    int_percent_t_al = int((round(percent_tc_alive / 5)))

    a = "*"
    espacio = " "

    un_a = int_percent_f * a
    dos_a = int_percent_s * a
    tres_a = int_percent_t * a
    cuatro_a = int_percent_f_al * a
    cinco_a = int_percent_s_al * a
    seis_a = int_percent_t_al * a

    r_1 = f"Total |{un_a + (20 - int_percent_f) * espacio}| {percent_fc}%\n"
    r_2 = f"Total |{dos_a + (20 - int_percent_s) * espacio}| {percent_sc}%\n"
    r_3 = f"Total |{tres_a + (20 - int_percent_t) * espacio}| {percent_tc}%\n"
    r_4 = f"Alive |{cuatro_a + (20 - int_percent_f_al) * espacio}| {percent_fc_alive}%\n"
    r_5 = f"Alive |{cinco_a + (20 - int_percent_s_al) * espacio}| {percent_sc_alive}%\n"
    r_6 = f"Alive |{seis_a + (20 - int_percent_t_al) * espacio}| {percent_tc_alive}%\n"

    fc_header = "== 1st Class ==\n"
    sc_header = "== 2nd Class ==\n"
    tc_header = "== 3rd Class ==\n"

    final_res = fc_header + r_1 + r_4 + sc_header + r_2 + r_5 + tc_header + r_3 + r_6
    
    return final_res


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(visualize((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (True, 2, 'Flunky Mr Hazelnut', 'female', 18, 51.2),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
    ]
)))
