from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

import numpy as np
import itertools

RIGHTGOING = ["-", "J", "7"]
LEFTGOING = ["-", "F", "L"]
UPGOING = ["|", "F", "7"]
DOWNGOING = ["|", "J", "L"]
CONNECTIONS = {
    "-":[(0,-1), (0,1)],
    "|":[(-1,0), (1,0)],
    "J":[(0,-1), (-1,0)],
    "7":[(0,-1), (1,0)],
    "F":[(1,0), (0,1)],
    "L":[(-1,0), (0,1)],
}

maze = np.array([[ch for ch in line] for line in inp.split("\n")])
start = np.array([[(i,j) for j, ch in enumerate(line) if ch=="S"] for i, line in enumerate(inp.split("\n")) if "S" in line]).flatten()
start = np.argwhere(maze == "S")[0]

i, j = start
connected = []
for (ii, jj), allowed_pipes in zip([(0,1), (0,-1), (1,0), (-1,0)], [RIGHTGOING, LEFTGOING, DOWNGOING, UPGOING]):
    if maze[i+ii, j+jj] in allowed_pipes:
        break

came_from = (i,j)
here = (i+ii, j+jj)
part_of_loop = set()
for n in itertools.count(start=1):
    i,j = here
    part_of_loop.add((i,j))
    if maze[i,j] == "S":
        break
    out_dirs = CONNECTIONS[maze[i,j]]
    for (ii,jj) in out_dirs:
        if (i+ii, j+jj) != came_from:
            break
    came_from = here
    here = (i+ii,j+jj)
print(n//2)
