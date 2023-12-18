from input_file import text_input
from itertools import cycle

# text_input="""RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""

# text_input="""LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

steps = 0

instructions = text_input.split("\n")[0]

directions_dictionary = {row[0] : tuple(row[1].strip("()").split(",")) for row in
                         [row.replace(" ", "").split("=") for row in text_input.split("\n")[2:]]}

start_position = "AAA"

for instruction in cycle(instructions):
    steps += 1
    
    start_position = directions_dictionary[start_position][0] \
        if instruction == "L" else directions_dictionary[start_position][1]
    
    if start_position == "ZZZ":
        break
            

print(steps)
