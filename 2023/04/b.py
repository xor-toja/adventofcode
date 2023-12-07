from input_file import text_input
from collections import defaultdict

# text_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

result = 0
winning_dict = defaultdict(lambda: 0)

for card_num, line in enumerate(text_input.split('\n'), 1):
    pre, post = line.split("|")
    pre = pre.strip()
    # remove unnecessary characters and create sets
    actual_numbers = " ".join(post.strip().split())
    winning_numbers = " ".join(pre.split(":")[1].split())
    actual_numbers = set(actual_numbers.split(" "))
    winning_numbers = set(winning_numbers.split(" "))

    winning_set = winning_numbers.intersection(actual_numbers)

    winning_dict[f"Card {card_num}"] += 1
    repeats =  winning_dict[f"Card {card_num}"]

    if not winning_set:
        continue

    for win in range(card_num + 1, card_num + len(winning_set) + 1):
        winning_dict[f"Card {win}"] += + repeats

for value in winning_dict.values():
    result += value

print(result)