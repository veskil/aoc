from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

import itertools
import math

instructions, node_list = inp.split("\n\n")

nodes: dict[str, dict[str, str]] = dict()
for node_def in node_list.split("\n"):
    here = node_def[0:3]
    left = node_def[7:10]
    right = node_def[12:15]
    nodes[here] = dict(L=left, R=right)

# Part 1
here = "AAA"
for i, inst in enumerate(itertools.cycle(instructions), start=1):
    here = nodes[here][inst]
    if here == "ZZZ":
        break
print(i)

# Part 2
starts = [node for node in nodes if node[-1] == "A"]
loop_times = []
for start in starts:
    here = start
    for i, inst in enumerate(itertools.cycle(instructions), start=1):
        here = nodes[here][inst]
        if here[-1] == "Z":
            break
    loop_times.append(i)
print(math.lcm(*loop_times))
