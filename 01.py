import re
f = open("01.input", "r")
input = [x for x in f]
strings = [re.findall('[0-9]', x) for x in input]
numbers = [int(x[0]+x[-1]) for x in strings]
print('Part 1:', sum(numbers))


digitsMap = {'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine': '9'}

matches = [re.finditer(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', x) for x in input]
strings2 = [[x.group(1) for x in match] for match in matches]
digits2 = [[digitsMap[d] if d in digitsMap else d for d in l] for l in strings2]
numbers2 = [int(x[0]+x[-1]) for x in digits2]
print('Part 2:', sum(numbers2))
