time, dist = [x.split()[1:] for x in list(open('06.input'))]

result = 1

for i, x in enumerate(time):
    ts = int(x)
    count = 0
    for t in range(1, ts):
        if (t * (ts-t) > int(dist[i])):
            count += 1
    result = result * count

print(result)

