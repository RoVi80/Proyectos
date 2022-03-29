import random

# These variables are required for the automatic grading to work, do not change
# their names. You can change values of these variables.
min_len_overall = 5
max_len_overall = 10
char_strt_overall = 43
char_end_overall = 57


def fuzzer(min_length, max_length, char_start, char_end):
    strng = ""
    for e in range(random.randint(min_length,max_length)):
        strng += chr(random.randint(char_start,char_end))
    return strng

def calculate_factorial(inp):
    fctorl = 1
    if inp == None:
        return None
    else:
        try:
            int(inp)
        except:
            raise TypeError("TypeError: string")
        else:
            intgr = int(inp)
        if intgr < 0:
            raise ValueError("ValueError: number negative")
        elif intgr > 10:
            raise ValueError("ValueError: number too large")
        else:
            for i in range(1, intgr+1):
                fctorl = fctorl*i
            return fctorl



def run(trials):
    fnl_lst = []
    if isinstance(trials, int) and trials > 0:
        for runs in range(trials):
            try:
                calculate_factorial(fuzzer(min_len_overall, max_len_overall, char_strt_overall, char_end_overall))
            except TypeError:
                success = 1
                strng = "Other error"
            except ValueError as err:
                success = 1
                strng =str(err)
            else:
                success = 0
                strng = ""


            fnl_lst.append((success,strng))
        return fnl_lst
    else:
        return []

print(run(5))