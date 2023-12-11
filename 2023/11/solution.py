from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

import numpy as np

universe = np.array([[(1 if ch=="#" else 0) for ch in line] for line in inp.split("\n")])
empty_rows = [i for i in range(len(universe)) if not np.any(universe[i])]
empty_cols = [j for j in range(len(universe[0])) if not np.any(universe[:,j])]
universe = np.insert(np.insert(universe, empty_rows, 0, axis=0), empty_cols, 0, axis=1)

positions = [ij for ij in np.ndindex(universe.shape) if universe[ij]]
total_distance = 0
for n, (i,j) in enumerate(positions):
    for (ii, jj) in positions[n+1:]:
        total_distance += abs(i-ii) + abs(j-jj)
print(total_distance)


universe = np.array([[(1 if ch=="#" else 0) for ch in line] for line in inp.split("\n")])
positions = np.array([list(ij) for ij in np.ndindex(universe.shape) if universe[ij]])
original_positions = np.copy(positions)

for i, row in enumerate(universe):
    if np.sum(row) == 0:
        positions[original_positions[:,0] > i, 0] += int(1e6) - 1
for j, col in enumerate(universe.T):
    if np.sum(col) == 0:
        positions[original_positions[:,1] > j, 1] += int(1e6) - 1

total_distance = 0
for n, (i,j) in enumerate(positions):
    for (ii, jj) in positions[n+1:]:
        total_distance += abs(i-ii) + abs(j-jj)
print(total_distance)
