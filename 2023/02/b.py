from input_file import text_input
from numpy import prod
# text_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

sum_ids = 0


for line in text_input.split("\n"):
    colors = {'red': 0, 'green': 0, 'blue': 0}
    game_id, games = line.split(":")
    games = games.strip().split(";")
    games = [game.split(",") for game in games]
    for inner_game in games:
        inner_game = [sub_game.strip() for sub_game in inner_game]
        break_contition = False
        for single_choice in inner_game:
            number, color = single_choice.split(" ")
            if colors[color] < int(number):
                colors[color] = int(number)
            print(colors)
    
    sum_ids += prod([items for items in colors.values()])

print("sum_ids:", sum_ids)