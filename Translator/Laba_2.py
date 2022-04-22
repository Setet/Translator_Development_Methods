import json


def priority(str):
    if str in ["R4", "R10", "АЭМ", "Ф", "W6", "W4", "W8", "W5"]:
        return 0
    if str in ["R5", "R11", "R6", "W3", "R9"]:
        return 1
    if str in ["O1", "W36", "W9"]:
        return 2
    if str == "O16":
        return 3
    if str == "O14":
        return 4
    if str == "O17":
        return 5
    if str in ["O10", "O12", "O25", "O24", "O11", "O13"]:
        return 6
    if str in ["O4", "O6"]:
        return 7
    if str in ["O2", "O8", "O9"]:
        return 8
    if str in ["O3", "O5", "O7"]:
        return 9
    if str in ["R8", "R12", "W29", "R13"]:
        return 10


def main():
    with open("I.json", "r") as read_file:
        I = json.load(read_file)

    with open("C.json", "r") as read_file:
        C = json.load(read_file)

    with open("N.json", "r") as read_file:
        N = json.load(read_file)

    with open('Лексемы.txt', 'r') as read_file:
        INPUT = read_file.read().split()

    STACK = []
    OUTPUT = []

    m = 0

    for i in range(len(INPUT)):
        lexem = INPUT[i]

        if lexem == "R2" or lexem in I.values() or lexem in C.values() or lexem in N.values():
            OUTPUT.append(lexem)
            continue

        if lexem == "R4" and i >= 1 and INPUT[i - 1] in I.values():
            STACK.append(1)
            STACK.append("Ф")
            continue

        if lexem == "R6":
            while STACK[len(STACK) - 1] != "АЭМ" and STACK[len(STACK) - 1] != "Ф" and STACK[len(STACK) - 1] != "ARR" and \
                    STACK[len(STACK) - 1] != "R4":
                if STACK[len(STACK) - 1] == "W36":
                    STACK.pop()
                    OUTPUT.append("БП")
                else:
                    OUTPUT.append(STACK.pop())
            op = STACK.pop()
            if op == "R4":
                STACK.append(1)
                STACK.append("ARR")
            else:
                STACK[len(STACK) - 1] += 1
                STACK.append(op)
            continue

        if lexem == "R4":
            STACK.append("R4")
            continue

        if lexem == "R10":
            STACK.append(2)
            STACK.append("АЭМ")
            continue

        if lexem == "W6":
            STACK.append("W6")
            continue

        if lexem == "W3":
            STACK.append("W3")
            continue

        if lexem == "W5":
            STACK.append("W5")
            continue

        if lexem == "W8":
            STACK.append("W8")
            continue

        if lexem == "W4":
            STACK.append("W4")
            continue

        if lexem == "W9":
            STACK.append("return")
            continue

        if lexem == "R7":
            if STACK[len(STACK) - 1] == "W5":
                OUTPUT.append(1)
                OUTPUT.append("НП")
            elif STACK[len(STACK) - 1] == "W8":
                OUTPUT.append("WH")
            elif STACK[len(STACK) - 1] == "W4":
                OUTPUT.append("FOR")
            elif STACK[len(STACK) - 1] == "W6":
                m += 1
                OUTPUT.append(f"M{m} УПЛ")
            elif STACK[len(STACK) - 1] == "W3":
                m += 1
                OUTPUT.append(f"M{m}")
                OUTPUT.append("БП")
                OUTPUT.append(f"M{m - 1}")
                OUTPUT.append(":")
            continue

        if lexem == "R13":
            if STACK[-1] == "W5" or STACK[-1] == "function":
                OUTPUT.append("КП")
            elif STACK[-1] == "W8" or STACK[-1] == "W4":
                OUTPUT.append("END")
            elif STACK[-1] == "W3":
                OUTPUT.append(f"M{m}")
                OUTPUT.append(":")
            STACK.pop()
            continue

        if lexem == "R9":
            while len(STACK) > 0 and STACK[-1] != "R4" and STACK[-1] != "W5" and STACK[-1] != "W6" and STACK[
                -1] != "W3" and STACK[-1] != "W4" and STACK[-1] != "W8" and STACK[-1] != "function":
                if STACK[len(STACK) - 1] == "W36":
                    STACK.pop()
                    OUTPUT.append("БП")
                else:
                    OUTPUT.append(STACK.pop())
            continue

        if lexem == "R5":
            while len(STACK) > 0 and STACK[len(STACK) - 1] != "R4" and STACK[len(STACK) - 1] != "Ф" and STACK[
                len(STACK) - 1] != "ARR":
                if STACK[len(STACK) - 1] == "W36":
                    STACK.pop()
                    OUTPUT.append("БП")
                else:
                    OUTPUT.append(STACK.pop())
            if len(STACK) > 0:
                op = STACK.pop()
                if op == "Ф":
                    if INPUT[i - 1] == "R4":
                        OUTPUT.append(STACK.pop())
                    else:
                        OUTPUT.append(STACK.pop() + 1)
                    OUTPUT.append("Ф")
                if op == "ARR":
                    OUTPUT.append(STACK.pop() + 1)
                    OUTPUT.append("ARR")

            continue

        if lexem == "R11":
            while STACK[len(STACK) - 1] != "АЭМ":
                if STACK[len(STACK) - 1] == "W36":
                    STACK.pop()
                    OUTPUT.append("БП")
                else:
                    OUTPUT.append(STACK.pop())
            STACK.pop()
            OUTPUT.append(STACK.pop())
            OUTPUT.append("АЭМ")
            continue

        if len(STACK) == 0 or priority(STACK[len(STACK) - 1]) < priority(lexem):
            STACK.append(lexem)
            continue

        while len(STACK) > 0 and priority(STACK[len(STACK) - 1]) >= priority(lexem):
            if STACK[len(STACK) - 1] == "W36":
                STACK.pop()
                OUTPUT.append("БП")
            else:
                OUTPUT.append(STACK.pop())
        STACK.append(lexem)

    while len(STACK) > 0:
        if STACK[len(STACK) - 1] == "W36":
            STACK.pop()
            OUTPUT.append("БП")
        else:
            OUTPUT.append(STACK.pop())

    with open("Лексемы_ОПН.txt", "w") as write_file:
        write_file.write(" ".join(map(str, OUTPUT)))


if __name__ == '__main__':
    main()
