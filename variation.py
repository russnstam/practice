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
    for a in e_list:
        num = set(a).intersection(set_list)
        if len(num) > 1:
            return False
        else:
            return True
    

def type_limit():
    while True:
        s = get_sets()
        g = get_germ()
        e_l = generate(s, g)
        bool_list = [rules(_) for _ in e_l[1]]
        if False in bool_list:
            continue
        else:
            return e_l

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

program_week(4)

