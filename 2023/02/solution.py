from pathlib import Path
inp = (Path(__file__).parent / "input.txt").read_text().strip("\n")

score = 0
max_per_color = {"red":12, "green":13, "blue":14}
for game_num, game in enumerate(inp.split("\n"), start=1):
    game = game.split(":")[1].strip()
    possible = True
    for draw in game.split("; "):
        for draw_part in draw.split(", "):
            num, color = draw_part.split(" ")
            num = int(num)
            if num > max_per_color[color]:
                possible = False
    if possible:
        score += game_num

print(score)

score = 0
for game_num, game in enumerate(inp.split("\n"), start=1):
    game = game.split(":")[1].strip()
    min_per_color = {"red":0, "green":0, "blue":0}
    for draw in game.split("; "):
        for draw_part in draw.split(", "):
            num, color = draw_part.split(" ")
            num = int(num)
            min_per_color[color] =  max(num, min_per_color[color])
    score += min_per_color["red"]*min_per_color["green"]*min_per_color["blue"]

print(score)
