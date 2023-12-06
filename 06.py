

def part1():
    time, dist = [x.split()[1:] for x in list(open('06.input'))]
    result = 1
    for i, x in enumerate(time):
        ts = int(x)
        count = 0
        for t in range(1, ts):
            if (t * (ts-t) > int(dist[i])):
                count += 1
        result = result * count
    return result

print("Part 1: ", part1())

def part2():
    time, dist = [int(x.split(":")[1].replace(" ", "")) for x in list(open('06.input'))]
    count = 0
    for t in range(1, time):
        if (t * (time-t) > dist):
            count += 1
    return count


print("Part 2: ", part2())
