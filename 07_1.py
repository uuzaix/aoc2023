import re
from functools import reduce
import operator

strength = {
    'A': 'a', 'K': 'b', 'Q':'c' ,'J':'d', 'T':'e', '9':'f', '8':'g', '7':'h', '6':'i', '5':'j', '4':'k', '3':'l', '2':'m'
}

with open ('07.input') as f:
    input = [x.split(" ") for x in f.read().split('\n')]


byType = [[] for _ in range(8)]
for turn in input:
    hand, bid = turn
    lettersHand= ''.join([strength[x] for x in hand])
    sortedHand = ''.join(sorted(lettersHand))
    matcher= re.compile(r'(.)\1*')
    cards = [match.group() for match in matcher.finditer(sortedHand)]

    sortedGroups = sorted(cards, key=len, reverse=True)

    if (len(sortedGroups[0]) == 5):
        byType[0].append([lettersHand, bid])
    elif (len(sortedGroups[0]) == 4):
        byType[1].append([lettersHand, bid])
    elif (len(sortedGroups[0]) == 3 and len(sortedGroups[1]) == 2):
        byType[2].append([lettersHand, bid])
    elif (len(sortedGroups[0]) == 3):
        byType[3].append([lettersHand, bid])
    elif (len(sortedGroups[0]) == 2 and len(sortedGroups[1]) == 2):
        byType[4].append([lettersHand, bid])
    elif (len(sortedGroups[0]) == 2):
        byType[5].append([lettersHand, bid])
    else: 
        byType[6].append([lettersHand, bid])

for i, type in enumerate(byType):
    if len(type)> 1:
        sortedType = sorted(type, key= lambda x: x[0])
        byType[i] = sortedType
finalList = reduce(operator.concat, byType)[::-1] 

sum = 0
for i, turn in enumerate(finalList):
    _, bid = turn
    sum += (i+1)*int(bid)
print("sum", sum)
    
