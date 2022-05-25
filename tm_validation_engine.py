import sys
from types import SimpleNamespace
import re

turingMachine = SimpleNamespace()

turingMachine.states, turingMachine.sigma, turingMachine.gama, turingMachine.delta = {}, {}, {}, {}
turingMachine.q0, turingMachine.qAccept, turingMachine.qFail = '', '', ''


def parseUselessLines(f):
    line = f.readline()

    if line != '':
        line = line.lstrip(' ').rstrip(' \n')

        while line == '' or line[:4] == '<!--':
            line = f.readline()

            if line == '':
                break

            line = line.lstrip(' ').rstrip(' \n')

    return line


def parseStates(f, turingMachine):
    line = parseUselessLines(f)

    if line == '---Start---':

        line = parseUselessLines(f)

        while line != '---End---':
            line = line.split(', ')

            if len(line) == 1:
                turingMachine.states[line[0]] = 1
            elif len(line) == 2:
                turingMachine.states[line[0]] = 1

                if line[1] == 'S':
                    turingMachine.q0 = line[0]
                elif line[1] == 'A':
                    turingMachine.qAccept = line[0]
                elif line[1] == 'F':
                    turingMachine.qFail = line[0]

            line = parseUselessLines(f)


def parseSigma(f, turingMachine):
    line = parseUselessLines(f)

    if line == '---Start---':

        line = parseUselessLines(f)

        while line != '---End---':
            line = line.split(' ')

            if len(line) == 1:
                turingMachine.sigma[line[0]] = 1

            line = parseUselessLines(f)


def parseGama(f, turingMachine):
    line = parseUselessLines(f)

    if line == '---Start---':

        line = parseUselessLines(f)

        while line != '---End---':
            line = line.split(' ')

            if len(line) == 1:
                turingMachine.gama[line[0]] = 1

            line = parseUselessLines(f)


def parseDelta(f, turingMachine):
    line = parseUselessLines(f)

    if line == '---Start---':

        line = parseUselessLines(f)

        while line != '---End---':
            line = re.split(', ', line)
            line[1] = line[1].split(' ')
            newLine = [line[0], line[1][0], line[1][2], line[2], line[3]]
            line = newLine

            if len(line) == 5:
                turingMachine.delta[(line[0], line[1])
                                    ] = (line[2], line[3], line[4])

            line = parseUselessLines(f)


def parsingFile(file, turingMachine=turingMachine):
    with open(file, 'r', encoding='utf-8') as f:
        line = parseUselessLines(f)

        while(line != ''):
            if line.lower() == 'states:':
                parseStates(f, turingMachine)

            line = parseUselessLines(f)

            if line.lower() == 'sigma:':
                parseSigma(f, turingMachine)

            line = parseUselessLines(f)

            if line.lower() == 'gama:':
                parseGama(f, turingMachine)

            line = parseUselessLines(f)

            if line.lower() == 'delta:':
                parseDelta(f, turingMachine)

            line = parseUselessLines(f)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        parsingFile('./' + sys.argv[1])

    print(turingMachine)
