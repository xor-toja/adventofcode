from functools import reduce
from input_file import text_input
from itertools import cycle
import math

# text_input="""LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

steps = []

instructions = text_input.split("\n")[0]

directions_dictionary = {row[0] : tuple(row[1].strip("()").split(",")) for row in
                         [row.replace(" ", "").split("=") for row in text_input.split("\n")[2:]]}

start_positions = [start for start in 
                   [row.replace(" ", "").split("=")[0] for row in text_input.split("\n")[2:]] 
                   if start.endswith("A")]

for start_position in start_positions:
    
    sep_step = 0
    for instruction in cycle(instructions):

        sep_step += 1        
        start_position = directions_dictionary[start_position][0] if instruction == "L" \
                          else directions_dictionary[start_position][1]
        
        if start_position.endswith("Z"):
            steps += [sep_step]
            break

lcm = reduce(lambda x, y: (x*y)//math.gcd(x,y), steps)
print(lcm)
