import sys
import tm_validation_engine as engine

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception("Too few arguments!")
    elif len(sys.argv) > 3:
        raise Exception("Too many arguments!")

    engine.parsingFile('./' + sys.argv[1])
    turingMachine = engine.turingMachine
    # print(turingMachine.states)
    # print(turingMachine.sigma)
    # print(turingMachine.gama)
    # print(turingMachine.delta)
    # print(turingMachine.q0)
    # print(turingMachine.qAccept)
    # print(turingMachine.qReject)
    tape = ['#'] * 10000
    inputText = sys.argv[2]

    for i in range(len(inputText)):
        tape[5000 + i] = inputText[i]

    head = turingMachine.q0
    pos = 5000

    hasReachedAState = -1

    while hasReachedAState == -1:
        letter = tape[pos]

        if head == turingMachine.qAccept:
            hasReachedAState = 1
            continue
        elif head == turingMachine.qReject:
            hasReachedAState = 0
            continue

        if turingMachine.delta.get((head, letter), 0):
            engineCurr = turingMachine.delta[(head, letter)]
            tape[pos] = engineCurr[1]
            head = engineCurr[0]
          #  print(engineCurr)
            pos = pos - 1 if engineCurr[2] == 'L' else pos + 1
        else:
            hasReachedAState = 0

    if hasReachedAState == 0:
        print("Gresit!")
    else:
        print("Corect!")
