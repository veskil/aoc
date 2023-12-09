from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

import numpy as np

sequences = np.array([[int(x) for x in line.split(" ")] for line in inp.split("\n")])

# Part 1
score = 0
for sequence in sequences:
    final_nth_diff = [sequence[-1]]
    diff = np.diff(sequence)
    while np.any(diff):
        final_nth_diff.append(diff[-1])
        diff = np.diff(diff)
    score += np.sum(final_nth_diff)
print(score)

# Part 2
score = 0
for sequence in sequences:
    first_nth_diff = [sequence[0]]
    diff = np.diff(sequence)
    while np.any(diff):
        first_nth_diff.append(diff[0])
        diff = np.diff(diff)
    score += np.sum([first_nth_diff[n]*(-1)**(n) for n in range(len(first_nth_diff))])
print(score)
