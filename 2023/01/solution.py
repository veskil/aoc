from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

from string import ascii_letters

number_words = "zero one two three four five six seven eight nine".split()

sol1 = 0
for line in inp.split("\n"):
    letters_removed = line.strip(ascii_letters)
    sol1 += int(letters_removed[0] + letters_removed[-1])
print(sol1)

sol2 = 0
for line in inp.split("\n"):
    for i, spelling in enumerate(number_words):
        line = line.replace(spelling, spelling + str(i) + spelling)
    letters_removed = line.strip(ascii_letters)
    sol2 += int(letters_removed[0] + letters_removed[-1])
print(sol2)
