from pathlib import Path
inp = (Path(__file__).parent / "example.txt").read_text().strip("\n")

import itertools

inp_blocks = inp.split("\n\n")

seeds = [int(x) for x in inp_blocks[0].split(": ")[1].split(" ")]
maps = [[[int(x) for x in line.split(" ")] for line in block.split("\n")[1:]] for block in inp_blocks[1:]]

seed_locations = []
for seed in seeds:
    source = seed
    dest = seed

    for m in maps:
        for (d, s, l) in m: # Destination, source, length
            if s <= source < s+l:
                dest = d + (source-s)
                break
        source = dest
    seed_locations.append(dest)
print(min(seed_locations))

# Part 2 (not complete)
class func:
    def __init__(self, mapping: list[tuple[int, int, int]]):
        self.x_break_points = []

    def __call__(self, x_range: tuple[int, int]) -> list[tuple[int, int]]:
        pass

# Seed ranges are inclusive on both ends
seed_ranges = [(x, x+l-1) for (x,l) in itertools.batched(seeds, 2)]
