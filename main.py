import random
num = [0, 1, 2]
X = '✖'
O = '◎'
plan = ["", "", ""]
plan[0] = [" ", " ", " "]
plan[1] = [" ", " ", " "]
plan[2] = [" ", " ", " "]
pos1 = random.choice(num)
pos2 = random.choice(num)
plan[pos1][pos2] = O
line = ""
def print_result():
 