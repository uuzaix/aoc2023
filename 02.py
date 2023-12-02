from functools import reduce

f = open("02.input", "r")
input = [x.replace(":", ";").replace('Game ', '').split(';') for x in f]
games = [[x.strip().split(', ') for i, x in enumerate(l)  if i > 0] for l in input]

def part1(games):
    rule = {'red': 12, 'green': 13, 'blue': 14}
    result = sum(range(101))
    for i, game in enumerate(games):
        impossible = 0
        for set in game:
            for color in set:
                cube = color.split(' ')
                if rule[cube[1]] < int(cube[0]):
                    impossible += 1
        if impossible > 0:
            result -= (i+1)
    return result

print ('Part 1:', part1(games))

def part2(games): 
    result = 0
    for game in games:
        minSet = {'red': 0, 'green': 0, 'blue': 0}
        for set in game:
            for color in set:
                cube = color.split(' ')
                if minSet[cube[1]] < int(cube[0]):
                    minSet[cube[1]] = int(cube[0])
        result += reduce((lambda x, y: x * y), minSet.values())
    return result

print ('Part 2:', part2(games))