import itertools

coordinates = []
with open ('11.input') as f:
    input = f.read().split('\n')
rowsToRepeat=[]
for x, row in enumerate(input):
    if '#' not in row:
        rowsToRepeat.append(x)
    else:
        for y, column in enumerate(row):
            if column == '#':
                coordinates.append([x, y])

columnsToRepeat = []
for i in range(len(input[0])):
    column = [x[i] for x in input]
    if "#" not in column:
        columnsToRepeat.append(i)

updatedcoordinates1 = []
updatedcoordinates2 = []
for p in coordinates:
    x, y = p
    increaseX = [i for i in rowsToRepeat if x > i]
    increaseY = [j for j in columnsToRepeat if y > j]
    diffX = len(increaseX)
    diffY = len(increaseY)
    updatedcoordinates1.append([x+ diffX, y + diffY])
    updatedcoordinates2.append([x+ diffX*(1000000 -1), y + diffY*(1000000- 1)])

def solve(coordinates):
    result = 0
    for pair in list(itertools.combinations(coordinates, 2)):
        a, b = pair
        distance = abs(a[0]-b[0]) + abs(a[1]-b[1])
        result += distance
    return result


print("Part1: ", solve(updatedcoordinates1))
print("Part2: ", solve(updatedcoordinates2))
    