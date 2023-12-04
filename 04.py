import re

cards = list(open('04.input'))
input = [x.strip().replace(":", "|").split('|')[1:] for x in cards]

result1 = 0
finalCards = []
for i, card in enumerate(input):   
    win = [int(x.group()) for x in re.finditer(r'\d+', card[0])]
    hand = [int(x.group()) for x in re.finditer(r'\d+', card[1]) if int(x.group()) in win]
    handLength = len(hand)
    if handLength > 0:
        result1 += pow(2, handLength - 1)
        for _ in range(1, 2 + finalCards.count(i)):
            finalCards.extend([x for x in range(i + 1, i + 1 + handLength)])

print("Part1: ", result1)
print("Part2: ", len(finalCards)+ len(input))