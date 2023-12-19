from input_file import text_input
from itertools import pairwise
from functools import reduce

# text_input = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

sequences = [map(int, x) for x in [x.split() for x in text_input.split("\n")]]

"""
0   3   6   9  12  15   B
  3   3   3   3   3   A
    0   0   0   0   0
"""

def differences(seq):
    return [b-a for a, b in pairwise(seq)]

def get_last(seq):
    *_, last = seq
    if all(s==0 for s in differences(seq)):
        return [last]
    return get_last(differences(seq)) + [last]

result = 0

for sequence in sequences:
    seq = list(sequence)
    result += reduce(lambda x, y: y + x, get_last(seq))

print(result)