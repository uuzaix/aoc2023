import re

with open ('03.input') as f:
    input = f.read().split('\n')

def findNumbersCoordinates():
    numbers = []
    for row, x in enumerate(input):
        numbersColumns = [[m.start(0), m.end(0) -1, int(m.group())] for m in re.finditer('[0-9]+', x)]
        numbers.append([row, numbersColumns])
    return numbers

def findSymbolsCoordinates(pattern, includeAll):
    symbols = []
    for row, x in enumerate(input):
        symbolColumns = [m.start(0) for m in re.finditer(pattern, x)]
        if len(symbolColumns) > 0 or includeAll:
            symbols.append([row, symbolColumns  ])
    return symbols

def getAdjacentNumbersToStars(numbersArray, symbolsArray, starsOnly):
    result = 0     
    for row in symbolsArray:
        symbolsRow, symbols = row
        for symbolCol in symbols:
            matches = []
            # check row above
            if symbolsRow-1 >= 0 and len(numbersArray[symbolsRow-1][1]) > 0:
                for num in numbersArray[symbolsRow-1][1]:
                    startCol, endCol, value = num
                    if startCol-1 <=  symbolCol <=  endCol+1:
                        matches.append(value)
            # check same row
            if len(numbersArray[symbolsRow][1]) > 0:
                for num in numbersArray[symbolsRow][1]:
                    startCol, endCol, value = num
                    if startCol-1 <=  symbolCol <=  endCol+1:
                        matches.append(value)
            # # check row below
            if symbolsRow+1 < len(numbersArray) and len(numbersArray[symbolsRow+1][1]) > 0:
                for num in numbersArray[symbolsRow+1][1]:
                    startCol, endCol, value = num
                    if startCol-1 <=  symbolCol <=  endCol+1:
                        matches.append(value)
            if starsOnly :
                if len(matches) == 2:
                    result += matches[0]*matches[1] 
            else:
                result += sum(matches)
    return result

numbersArray = findNumbersCoordinates()
symbols = findSymbolsCoordinates('[^0-9.]', True)
stars = findSymbolsCoordinates('[*]', False)

print("Part 1:", getAdjacentNumbersToStars(numbersArray, symbols, False))
print("Part 2:", getAdjacentNumbersToStars(numbersArray, stars, True))