from input_file import text_input

# text_input="""seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4
# """

seeds = [int(x) for x in text_input.split("\n")[0].split(":")[1].split()]

# both sides closed >> [x,y]
seeds = [(x,x+y-1) for x,y in zip(seeds[::2], seeds[1::2])]

for line in text_input.split("\n")[2:]:
    if line.endswith("map:"):
        mapping_dict = {}
        continue

    if not line:
        temporary_seed_range = []
        while seeds:
            current_seed_range = seeds.pop(0)
            for mapping, offset in mapping_dict.items():
                if current_seed_range[0] >= mapping[0] \
                and current_seed_range[1] <= mapping[1]:
                    temporary_seed_range += \
                        [tuple(r + offset for r in current_seed_range)]
                    break
                if current_seed_range[0] <= mapping[0] \
                and current_seed_range[1] >= mapping[1]:
                    temporary_seed_range += [(mapping[0] + offset, mapping[1] + offset)]
                    seeds += [(current_seed_range[0], mapping[0] - 1)]
                    seeds += [(current_seed_range[1] + 1, mapping[1])]
                    break
                if current_seed_range[0] > mapping[1] \
                or current_seed_range[1] < mapping[0]:
                    continue
                if current_seed_range[0] < mapping[0]:
                    temporary_seed_range += [(mapping[0] + offset, current_seed_range[1] + offset)]
                    seeds += [(current_seed_range[0], mapping[0] - 1)]
                    break
                if current_seed_range[1] > mapping[1]:
                    temporary_seed_range += [(current_seed_range[0] + offset, mapping[1] + offset)]
                    seeds += [(mapping[1] + 1, current_seed_range[1])]
                    break

            else:
                temporary_seed_range += [current_seed_range]
        seeds = temporary_seed_range.copy()
        continue

    dst, src, rng = (int(x) for x in line.split())
    mapping_dict[(src,src+rng-1)] = dst - src


print(min(x[0] for x in seeds))

