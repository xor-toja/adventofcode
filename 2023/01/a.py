from input_file import text_input

result = 0

for line in text_input.split("\n"):
    if not line:
        continue
    numbers = "".join(t for t in line if t.isnumeric())

    result += int(numbers[0]+numbers[-1:])

print(result)