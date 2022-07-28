import sys
import tm_validation_engine as engine


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception("Too few arguments!")
    elif len(sys.argv) > 3:
        raise Exception("Too many arguments!")

    engine.parseAndVerify('./' + sys.argv[1])

    turingMachine = engine.turingMachine
    # print(turingMachine.states)
    # print(turingMachine.sigma)
    # print(turingMachine.gama)
    # print(turingMachine.delta)
    # print(turingMachine.q0)
    # print(turingMachine.qAccept)
    # print(turingMachine.qReject)
    tapes = [['^'] * 10000] * 2
    inputText = sys.argv[2]

    for letter in inputText:
        if turingMachine.sigma.get(letter, 0) == 0:
            raise Exception('The input is not a valid one!')

    for i in range(len(inputText)):
        tapes[0][5000 + i], tapes[1][5000 + i] = inputText[i], inputText[i]

    head = turingMachine.q0
    pos = 5000

    hasReachedAState = -1

    while hasReachedAState == -1:
        letter = tapes[0][pos]

        if turingMachine.delta.get((head, letter), 0):
            engineCurr = turingMachine.delta[(head, letter)]
            tapes[0][pos], tapes[1][pos] = engineCurr[1], engineCurr[1]
            if tapes[0][pos] != tapes[1][pos]:
                raise Exception(
                    "The copy of the first tape couldn't be maintained")
            head = engineCurr[0]

            if head == turingMachine.qAccept:
                hasReachedAState = 1
                continue
            elif head == turingMachine.qReject:
                hasReachedAState = 0
                continue
          #  print(engineCurr)
            if engineCurr[2] == 'L':
                pos -= 1
            else:
                pos += 1
        else:
            hasReachedAState = 0

    def finalState():
        print("Wrong!")

    if hasReachedAState == 0:
        print("Wrong!")
    else:
        # print("here")
        semafor = 0

        for i in range(len(tapes[0])):
            if tapes[0][i] != tapes[1][i]:
                finalState()
                semafor = 1

        if semafor == 0:
            print("Correct!")
