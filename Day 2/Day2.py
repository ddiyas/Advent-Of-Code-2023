file = open("Day 2\input.txt")
input_txt = file.read()

input = input_txt.split("\n")

sum = 0

def __sum__ (values):
    sum = 0
    for x in values:
        sum += x
    return sum

for line in input:
    game_index = line[line.index("Game") + 5 : line.index(":")]
    trial = line[line.index(game_index) + len(game_index) + 2 :].split(";")
    max_red = 0
    max_green = 0
    max_blue = 0
    for t in trial:
        green = 0
        blue = 0
        red = 0
        colors = t.split(",")
        for c in colors:
            if c.__contains__("green"):
                green = (int(c[:c.index("green")].strip()))
            elif c.__contains__("blue"):
                blue = (int(c[:c.index("blue")].strip()))
            elif c.__contains__("red"):
                red = (int(c[:c.index("red")].strip()))
                
        if red > max_red:
            max_red = red
        if blue > max_blue:
            max_blue = blue
        if green > max_green:
            max_green = green

    sum += max_red * max_blue * max_green

print(sum)  