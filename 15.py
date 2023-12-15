with open('15.input') as f:
    data = f.read().split(',')

def solve1(data):
    result = 0
    for string in data:
        value = 0
        for char in string:
            asciiValue = ord(char)
            value += asciiValue
            value *= 17
            value = value % 256
        result += value
    return result
print("Part 1: ", solve1(data))


def getLens(string):
    hash = 0
    if '-' in string:
        label = string.split("-")[0]
        action = '-'
        length = 0
    if '=' in string:
        label, length = string.split("=")
        action = '+'

    for char in label:
        asciiValue = ord(char)
        hash += asciiValue
        hash *= 17
        hash = hash % 256
    return [action, hash, label, length]

def addLens(b, label, length):
    box = b
    for i, lens in enumerate(box):
        if lens[0] == label:
            box[i] = [label, length]
            return box
    box.append([label, length])
    return box

def removeLens(box, label):
    if len(box) > 0:
        for i, lens in enumerate(box):
            if lens[0] == label:
                return box[:i] + box[i+1:]
    return box

def fillBoxes(data):
    boxes = [[] for _ in range(256)]
    for string in data:
        action, boxId, label, length = getLens(string)
        if action == '+':
            newBox = addLens(boxes[boxId], label, length)
            boxes[boxId] = newBox
        if action == '-':
            newBox = removeLens(boxes[boxId],label)
            boxes[boxId] = newBox
    return boxes

def solve2(data):
    result = 0
    boxes = fillBoxes(data)
    for i, box in enumerate(boxes):
        if len(box) > 0:
            for j, lens in enumerate(box):
                _, length = lens
                result += (i+1)*(j+1)*int(length)
    return result

print('Part2: ', solve2(data))
