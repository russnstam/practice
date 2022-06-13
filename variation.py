import pandas as pd
import random

def get_germ():
    seed = list(range(9))
    return random.sample(seed, len(seed))

def get_sets():
    set_num = [2, 2, 2, 3]
    return random.sample(set_num, len(set_num))

df = pd.read_csv('Variation Matrix.csv')

def generate(sets_num, germ):
    sets = []
    num_sets = []
    total = 0
    choices = ["Option1", "Option2", "Option3"]
    for i in sets_num:
        counter = 0
        round = []
        num_round = []
        while counter < i:
            sel = df.at[germ[total],(random.choice(choices))]
            sel_num = germ[total]
            if not pd.isna(sel):
                round.append(sel)
                num_round.append(sel_num)
                counter += 1
                total += 1     
            else:
                counter = counter
        sets.append(round)
        num_sets.append(num_round)
    return(sets, num_sets)

# Function to enforce rules for exercise allowances within set
def rules(set_list):
    # set_list represents the superset being checked
    e_list = [[0,1,2,3],[4,5,6],[7,8]]
    # e_list represents the exercise zones
    check_list = []
    for a in e_list:
        num = set(a).intersection(set_list)
        if len(num) > 1:
            check_list.append(False)
        else:
            check_list.append(True)
    return check_list

def type_limit():
    counter = 0
    while counter == 0:
        s = get_sets()
        g = get_germ()
        e_l = generate(s, g)
        bool_list = [rules(_) for _ in e_l[1]]
        if False in checker(bool_list):
            counter = counter
        else:
            return e_l

def checker(bool_list):
    checker = []
    for i in bool_list:
        if False in i:
            checker.append(False)
        else:
            checker.append(True)
    return checker
        
def program_week(num):
    count = ['One', 'Two', 'Three', 'Four']
    for d in range(num):
        print()
        print(f"Day {count[d]} Workout:")
        counter = 0
        for i in type_limit()[0]:
            print(f"Set {count[counter]}:")
            counter += 1
            for x in i:
                print(x)
    print()

program_week(3)
