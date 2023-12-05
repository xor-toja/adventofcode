from input_file import text_input
from collections import OrderedDict
from itertools import product

# text_input = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

# create point class

class Point:
    def __init__(self, x, y, value) -> None:
        self.x = [x]
        self.y = y
        self.value = value

    def __add__(self, other):
        self.value += other.value
        self.x += other.x
        return self

    def __repr__(self) -> str:
        return f"Point(x={self.x},y={self.y},val={self.value})"

special_chars = []
points = OrderedDict()
result = 0

# create list/dict of points

for y, row in enumerate(text_input.split("\n")):
    for x, col in enumerate(row):
        point = Point(x,y,col)
        if col.isdigit():
            try:
                last_key = next(reversed(points))
            except StopIteration:
                points[(x,y)] = point
            else:
                if points[last_key].y == y and x-1 in points[last_key].x:
                    points[last_key] += point
                else:
                    points[(x,y)] = point
        elif col != ".":
            special_chars.append((x,y))

# find touch-point, check if they containt special char and add value if so

for point in points.values():
    min_x = min(point.x) - 1
    max_x = max(point.x) + 1

    y_list = (y for y in range(point.y - 1, point.y + 2))
    x_list = (x for x in range(min(point.x) - 1, max(point.x) + 2))

    number_itself = ((x,point.y) for x in point.x)
    touch_points = list(product(x_list, y_list))

    for coord in number_itself:
        touch_points.remove(coord)

    if any(touch_point in special_chars for touch_point in touch_points):
        result += int(point.value)

print(result)