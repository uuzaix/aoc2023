import math
with open ('08.input') as f:
    input = [x for x in f.read().split('\n')if x != '']

instrs = input[0]
network = {}
for step in input[1:]:
    s, e = step.replace(" ", "").split("=")
    r,l = e.replace("(", "").replace(")", "").split(",")
    network[s] = [r, l]

def walk1(start, steps):
    count = steps
    loc = start
    for instr in instrs:
        count += 1
        index = 0 if instr == "L" else 1
        loc = network[loc][index]
        if loc == "ZZZ":
            return count
    return walk1(loc, count)

def walk2(start, steps):
    count = steps
    loc = start
    for instr in instrs:
        count += 1
        index = 0 if instr == "L" else 1
        loc = network[loc][index]
        if loc.endswith("Z"):
            return count
    return walk2(loc, count)


print("Part 1: ", walk1("AAA", 0))

def solve2():
    result = 1
    allWithA = [x for x in network.keys() if x.endswith("A")]
    for loc in allWithA:
        t = walk2(loc, 0)
        result = math.lcm(result, walk2(loc, 0))
    return result
print("Part 2: ", solve2())