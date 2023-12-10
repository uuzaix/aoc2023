with open ('09.input') as f:
    input = [x.split(" ") for x in f.read().split('\n')if x != '']

def diff(row):
    return [int(row[i+1])-int(x) for i, x in enumerate(row) if i < len(row) -1]

def solveRow(rows):
    if len([x for x in rows[-1] if x != 0]) == 0:
        return rows
    else:
        rowDiff = diff(rows[-1])
        return solveRow(rows +[rowDiff])



def solve():
    count1 = 0
    count2 = 0
    for row in input:
        introw = [int(x) for x in row]
        res = solveRow([introw])
        count1 += sum([x[-1] for x in res])
        count2 +=  sum([x[0] for i, x in enumerate(res) if i %2 == 0]) - sum([x[0] for i, x in enumerate(res) if i % 2 != 0])

    return (count1, count2)

print("Result: ", solve())