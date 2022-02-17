#!/usr/bin/env python3

import sys
import re
import random

def printInvalidInput(roll):
    print("Input \"%s\" is invalid" % roll)

def main():
    argc = len(sys.argv)
    argv = sys.argv

    if argc < 2:
        print("Must supply argument to describe the roll")
        return 1

    roll = argv[1]

    m = re.search("(\\d*)[d,D](\\d*)$", roll)
    if m:
        g1 = m.group(1)
        g2 = m.group(2)
        if g1 == "" and g2 == "":
            printInvalidInput(roll)
            return 1
        elif g1 != "":
            numDice = int(m.group(1))
        else:
            numDice = 1

        numSides = int(m.group(2))

        output = []
        for i in range(numDice):
            output.append(random.randint(1, numSides))
        print(output)
    else:
        printInvalidInput(roll)
        return 1


if __name__ == "__main__":
    main()
