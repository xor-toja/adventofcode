from input_file import text_input

# text_input="""Time:      7  15   30
# Distance:  9  40  200"""

time_allowed, distance_record = text_input.split("\n")
time_allowed = tuple(map(int, time_allowed.split(":")[1].strip().split()))
distance_record = tuple(map(int, distance_record.split(":")[1].strip().split()))

result = 1

def possible_distances(time_allowed):
    for t in range(1, time_allowed + 1):
        yield (time_allowed - t) * t

for ta, dr in zip(time_allowed, distance_record):
    result *= len([d for d in possible_distances(ta) if d > dr])

print(result)