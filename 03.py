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

def getAdjacentNumbersToAnySymbol():
    numbersArray = findNumbersCoordinates()
    symbols = findSymbolsCoordinates('[^0-9.]', True)
    result = 0    
    for row in numbersArray:
        numbersRow, numbers = row
        if len(numbers) > 0:
            for number in numbers:
                startCol, endCol, value = number
                match = 0
                # check row above
                if numbersRow-1 >= 0 and len(symbols[numbersRow-1][1]) > 0:
                    for symCol in symbols[numbersRow-1][1]:
                        if startCol-1 <=  symCol <=  endCol+1:
                            match +=1
                # check same row
                if len(symbols[numbersRow][1]) > 0:
                    for symCol in symbols[numbersRow][1]:
                        if startCol-1 <=  symCol <=  endCol+1:
                            match +=1
                # check row below
                if numbersRow+1 < len(symbols) and len(symbols[numbersRow+1][1]) > 0:
                    for symCol in symbols[numbersRow+1][1]:
                        if startCol-1 <=  symCol <=  endCol+1:
                            match +=1
                if match > 0:
                    result += value 
    return result


def getAdjacentNumbersToStars():
    numbersArray = findNumbersCoordinates()
    symbolsArray = findSymbolsCoordinates('[*]', False)
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
            if len(matches) == 2:
               result += matches[0]*matches[1] 
    return result

print("Part 1:", getAdjacentNumbersToAnySymbol())
print("Part 2:", getAdjacentNumbersToStars())

