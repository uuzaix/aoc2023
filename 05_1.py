import re

with open ('05.input') as f:
    input = [x for x in f.read().split('\n')if x != '']
seeds1 = [int(x) for x in input[0].split(':')[1].strip().split(' ')]

seedToSoilInx = input.index('seed-to-soil map:')
soilToFertInx = input.index('soil-to-fertilizer map:')
fertToWaterInx = input.index('fertilizer-to-water map:')
waterToLightInx = input.index('water-to-light map:')
lightToTempInx = input.index('light-to-temperature map:')
tempToHumInx = input.index('temperature-to-humidity map:')
humToLocInx = input.index('humidity-to-location map:')

seedToSoil = input[seedToSoilInx+1:soilToFertInx]
soilToFertInx = input[soilToFertInx+1:fertToWaterInx]
fertToWaterInx = input[fertToWaterInx+1:waterToLightInx]
waterToLightInx = input[waterToLightInx+1:lightToTempInx]
lightToTempInx = input[lightToTempInx+1:tempToHumInx]
tempToHumInx = input[tempToHumInx+1:humToLocInx]
humToLocInx = input[humToLocInx+1:]

def isInRange(value, sourceStart, range):
    return sourceStart <= value <= sourceStart + range

def translateValue(value, sourceStart, destStart):
    return destStart + (value- sourceStart)


def iterate(value, valuesMap):
    for m in valuesMap:
        destStart, sourceStart, range  = [int(x) for x in m.split(" ")]
        if isInRange(value, sourceStart, range - 1):
            return translateValue(value, sourceStart, destStart)
    return value


def solve(seeds):
    result = []
    for seed in seeds:
        maps = [seedToSoil, soilToFertInx, fertToWaterInx, waterToLightInx, lightToTempInx, tempToHumInx, humToLocInx]
        value = seed
        for m in maps:
            value = iterate(value, m)
        result.append(value)
    return result


print("Part 1:", min(solve(seeds1)))     
