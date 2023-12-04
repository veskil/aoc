from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

cards = inp.split("\n")

# Part 1
score = 0
for card in cards:
    card = card.split(": ")[1]
    got, goal = card.split(" | ")
    got_numbers = [int(s.strip()) for s in got.split(" ") if s]
    goal_numbers = [int(s.strip()) for s in goal.split(" ") if s]
    matches = len(set(got_numbers).intersection(set(goal_numbers)))
    if matches != 0:
        score += int(2**(matches-1))
print(score)


# Part 2
num_cards = len(cards)
card_copies = {i:1 for i in range(num_cards)}

for i, card in enumerate(cards):
    card = card.split(": ")[1]
    got, goal = card.split(" | ")
    got_numbers = [int(s.strip()) for s in got.split(" ") if s]
    goal_numbers = [int(s.strip()) for s in goal.split(" ") if s]
    matches = len(set(got_numbers).intersection(set(goal_numbers)))
    for j in range(matches):
        card_copies[i+1+j] += card_copies[i]

score = sum(card_copies.values())
print(score)
