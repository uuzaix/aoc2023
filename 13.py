import itertools

def transpose(pattern):
    transposed = []
    for i in range(len(pattern[0])):
        transposed.append("".join([row[i] for row in pattern]))
    return transposed 

def findVertical(pattern):
    return findHorizontal(transpose(pattern))

def findHorizontal(pattern):
    for i in range(1, len(pattern)):
        isMatch = True
        for j in range(1,i+1):
            if i+j-1 >= len(pattern):
                break
            if pattern[i+j-1] != pattern[i-j]:
                isMatch = False
                break
        if isMatch:
            return i
    return 0


def solve1():
    with open ('13.input') as f:
        input = [x for x in f.readlines()]

    patterns = [list(y) for x, y in itertools.groupby(input, lambda z: z == "") if not x]

    count = 0
    for pattern in patterns:
        result = findVertical(pattern)
        if result == 0:
            result = findHorizontal(pattern)
            count += 100*result
        else:
            count += result
    return count


print("P1:", solve1() )




