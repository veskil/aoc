from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

import re
import string

symbols = string.punctuation.replace(".", "")

# Pad with "." to avoid index bound errors
inp = "."*(inp.find("\n")+1) + "\n" + inp + "\n" + "."*(inp.find("\n")+1)
inp = inp.replace("\n", ".\n.")

lines = inp.split("\n")

# 1
score = 0
for i, line in enumerate(lines):
    for number in re.finditer("\d+", line):
        if any([
                any([char in symbols for char in lines[ii][number.start()-1:number.end()+1]])
                for ii in range(i-1,i+2)]):
            score += int(number.group())
print(score)

# 2
score = 0
for i, line in enumerate(lines):
    for symb in re.finditer("\*", line):
        j_symb = symb.start()
        adjacent_nums = []

        for ii in (i-1, i, i+1):
            for number in re.finditer("\d+", lines[ii]):
                if number.start() - 1 <= j_symb < number.end() + 1:
                    adjacent_nums.append(int(number.group()))
        if len(adjacent_nums) == 2:
            score += adjacent_nums[0] * adjacent_nums[1]
print(score)
