from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

PART = 2

if PART == 1:
    CARD_VALUE = {str(i):i for i in range(2,10)} | dict(T=10, J=11, Q=12, K=13, A=14)
    def get_hand_type(hand: list[int]) -> int:
        uniques = set(hand)
        counts = sorted([hand.count(x) for x in uniques], reverse=True)
        ordering = [[1,1,1,1,1], [2,1,1,1], [2,2,1], [3,1,1], [3,2], [4,1], [5]]
        return ordering.index(counts)
else:
    CARD_VALUE = {str(i):i for i in range(2,10)} | dict(T=10, J=1, Q=12, K=13, A=14)
    def get_hand_type(hand: list[int]) -> int:
        uniques = set(hand)
        counts = sorted([hand.count(x) for x in uniques], reverse=True)
        jokers = hand.count(1)
        ordering = [[1,1,1,1,1], [2,1,1,1], [2,2,1], [3,1,1], [3,2], [4,1], [5]]
        type_before_jokers = ordering.index(counts)

        if not jokers:
            return type_before_jokers
        match type_before_jokers:
            case 0:
                return type_before_jokers + 1
            case 1:
                return type_before_jokers + 2
            case 2:
                return type_before_jokers + (3 if jokers==2 else 2)
            case 3:
                return type_before_jokers + 2
            case _:
                return 6

hands = []
for line in inp.split("\n"):
    cards, bid = line.split(" ")
    card_values = [CARD_VALUE[card] for card in cards]
    hands.append((card_values, get_hand_type(card_values), int(bid)))

score = 0
for cards, hand_type, bid in hands:
    rank = 1
    for other_cards, other_hand_type, _ in hands:
        if hand_type > other_hand_type:
            rank += 1
        elif hand_type == other_hand_type:
            for card, other_card in zip(cards, other_cards):
                if other_card > card:
                    break
                if card > other_card:
                    rank += 1
                    break
    score += rank * bid
print(score)
