from input_file import text_input
# text_input = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""

allowed_numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                    "1", "2", "3", "4", "5", "6", "7", "8", "9")

result = 0

for line in text_input.split("\n"):
    if not line:
        continue

    l_find_dict = {}
    r_find_dict = {}

    for word in allowed_numbers:
        l_find_dict[word] = line.find(word)
        r_find_dict[word] = line.rfind(word)

    l_find_dict = {key:value for key,value in l_find_dict.items() if value >= 0}
    r_find_dict = {key:value for key,value in r_find_dict.items() if value >= 0}

    first = min(l_find_dict, key=l_find_dict.get)
    last = max(r_find_dict, key=r_find_dict.get)

    translator = {"one":"1", "two":"2", "three":"3", "four":"4",
                  "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    first = first if first not in translator else translator[first]
    last = last if last not in translator else translator[last]

    result += int(first+last)


print(result)
