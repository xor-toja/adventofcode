from input_file import text_input
from collections import OrderedDict

text_input="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

seeds = [int(seed) for seed in text_input.split("\n")[0].split(":")[1].split()]
paths = []

for line in text_input.split("\n")[2:]:
    if "map" in line:
        mapping_dict = OrderedDict()
        continue

    if not line:
        paths.append(mapping_dict)
        continue

    dest, rang, amnt = map(int, line.split())
    mapping_dict[f"{rang}-{rang + amnt}"] = dest - rang


# idx = 0
# temp
# for rang, offset in mapping_dict.items():
#     if idx % 2 != 0:

#     else:
#         seeds = [seed for seed in seeds if ]

print(paths)