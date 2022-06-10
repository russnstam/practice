import random

start = list(range(9))

upper = [0,1,2,3]
lower = [4,5,6]
core = [7,8]
cntrl_rand = []

for i in list(range(9)):
    num = random.choice(start)
    