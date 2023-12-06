from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

# d = x * (x_max - x)
# dd/dx = -2x + x_max = 0 => x = x_max/2

times, distances = [[int(x.strip()) for x in line.split(":")[1].split(" ") if x] for line in inp.split("\n")]

# Part 1
score = 1
for time, distance in zip(times, distances):
    ways_to_win = 0
    button_time = time//2
    while button_time * (time - button_time) > distance:
        ways_to_win += 2
        button_time -= 1
    if time%2 == 0:
        ways_to_win -= 1
    score *= ways_to_win
print(score)

# Part 2
time = int("".join([str(x) for x in times]))
distance = int("".join([str(x) for x in distances]))
ways_to_win = 0
button_time = time//2
while button_time * (time - button_time) > distance:
    ways_to_win += 2
    button_time -= 1
if time%2 == 0:
    ways_to_win -= 1
print(ways_to_win)
