from input_file import text_input
from collections import Counter

class Card:

    _ordered_ranks = "23456789TJQKA"

    def __init__(self, rank) -> None:
        self.rank = rank

    def __repr__(self) -> str:
        return f"Card(rank={self.rank})"

    def __eq__(self, other) -> bool:
        return self.rank == other.rank

    def __lt__(self, other) -> bool:
        return Card._ordered_ranks.index(self.rank) \
                < Card._ordered_ranks.index(other.rank)

class Hand:

    _ordered_strength = ["high-card",
                         "one-pair",
                         "two-pair",
                         "three-of-a-kind",
                         "full-house",
                         "four-of-a-kind",
                         "five-of-a-kind"]

    def __init__(self, cards) -> None:
        self.cards = cards

    def __lt__(self, other) -> bool:
        if self.strength == other.strength:
            for c1, c2 in zip(self.cards, other.cards):
                if c1 == c2: continue
                return c1 < c2

        return Hand._ordered_strength.index(self.strength) \
                < Hand._ordered_strength.index(other.strength)

    def __repr__(self) -> str:
        return "Hand(" + "".join(card.rank for card in self.cards) + ")"

    @property
    def strength(self):
        ranks = "".join(card.rank for card in self.cards)
        cnt = list(Counter(ranks).values())
        if 5 in cnt:
            return "five-of-a-kind"
        if 4 in cnt:
            return "four-of-a-kind"
        if 3 in cnt and 2 in cnt:
            return "full-house"
        if 3 in cnt:
            return "three-of-a-kind"
        if cnt.count(2) == 2:
            return "two-pair"
        if 2 in cnt:
            return "one-pair"
        return "high-card"


# text_input="""32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

cards_bids = text_input.split("\n")
cards_bids = [tuple(c.split()) for c in cards_bids]

hands_bids = [(Hand(list(Card(c) for c in cards)), bids) for cards, bids in cards_bids]

result = 0

for rank, sorted_hand in enumerate(sorted(hands_bids, key=lambda x: x[0]), start=1):

    result += rank * int(sorted_hand[1])

print(result)
