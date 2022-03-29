#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gender_class_rates(dataset):

    total_p = 0
    mp = 0
    fp = 0
    fcm = 0
    scm = 0
    tcm = 0
    fcf = 0
    scf = 0
    tcf = 0

    for i in dataset[1]:
        i_list = list(i)

        if i[3] == "male":
            mp += 1
            if i_list[1] == 1:
                fcm += 1
            if i_list[1] == 2:
                scm += 1
            if i_list[1] == 3:
                tcm += 1
        
        if i[3] == "female":
            fp += 1
            if i_list[1] == 1:
                fcf += 1
            if i_list[1] == 2:
                scf += 1
            if i_list[1] == 3:
                tcf += 1

        total_p += 1
    
    fc_male = float(fcm) / float(total_p)
    fc_female = float(fcf) / float(total_p)
    sc_male = float(scm) / float(total_p)
    sc_female = float(scf) / float(total_p)
    tc_male = float(tcm) / float(total_p)
    tc_female = float(tcf) / float(total_p)

    round_fcm = round(fc_male, 3)
    round_fcf = round(fc_female, 3)
    round_scm = round(sc_male, 3)
    round_scf = round(sc_female, 3)
    round_tcm = round(tc_male, 3)
    round_tcf = round(tc_female, 3)

    res_fm = round_fcm * 100
    res_sm = round_scm * 100
    res_tm = round_tcm * 100
    res_ff = round_fcf * 100
    res_sf = round_scf * 100
    res_tf = round_tcf * 100

    round_res_fm = round(res_fm, 1)
    round_res_sm = round(res_sm, 1)
    round_res_tm = round(res_tm, 1)
    round_res_ff = round(res_ff, 1)
    round_res_sf = round(res_sf, 1)
    round_res_tf = round(res_tf, 1)

    if round_res_fm == 0:
        round_res_fm = None
    if round_res_sm == 0:
        round_res_sm = None
    if round_res_tm == 0:
        round_res_tm = None
    if round_res_ff == 0:
        round_res_ff = None
    if round_res_sf == 0:
        round_res_sf = None
    if round_res_tf == 0:
        round_res_tf = None


    final_tuple = ((round_res_fm, round_res_sm, round_res_tm), (round_res_ff, round_res_sf, round_res_tf))
    return final_tuple
print(gender_class_rates((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
        # ...
    ]
)))
