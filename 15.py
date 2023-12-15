with open('15.input') as f:
    data = f.read().split(',')

result = 0
for string in data:
    value = 0
    for char in string:
        asciiValue = ord(char)
        value += asciiValue
        value *= 17
        value = value % 256
    result += value

print(result)