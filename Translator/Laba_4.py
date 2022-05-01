import json


def main():
    with open("I.json", "r") as read_file:
        I = json.load(read_file)

    with open("C.json", "r") as read_file:
        C = json.load(read_file)

    with open("N.json", "r") as read_file:
        N = json.load(read_file)

    with open("O.json", "r") as read_file:
        O = json.load(read_file)

    with open("W.json", "r") as read_file:
        W = json.load(read_file)

    with open('Лексемы.txt', 'r') as read_file:
        INPUT = read_file.read().split()

    STACK = []
    OUTPUT = []

    number_of_mistakes = 0
    massiv_of_mistakes = []

    for i in range(len(INPUT)):
        lexem = INPUT[i]

        if i + 1 < len(INPUT):

            # func
            if lexem == "W5":
                OUTPUT.append(lexem)
                continue

            # var+let+new
            if lexem == "W7" or lexem == "W21" or lexem == "W10" and INPUT[i + 1] == I.values:
                OUTPUT.append(lexem)
                continue

            # for+if+elif+else+while+return+do+switch
            if lexem == "W4" or lexem == "W6" or lexem == "W12" or lexem == "W8" or lexem == "W3" or lexem == "W9" or \
                    lexem == "W11" or lexem == "W13" and INPUT[i + 1] == "R4":
                OUTPUT.append(lexem)
                continue

            # case
            if lexem == "W14" and INPUT[i + 1] == I.values or INPUT[i + 1] == C.values or INPUT[i + 1] == N.values:
                OUTPUT.append(lexem)
                continue

            # this
            if lexem == "W15" and INPUT[i + 1] == "R7":
                OUTPUT.append(lexem)
                continue

            # try+catch
            if lexem == "W16" and INPUT[i + 1] == "R12" or lexem == "W17" and INPUT[i + 1] == "R12":
                OUTPUT.append(lexem)
                continue

            # alert+promt+confirm
            if lexem == "W22" or lexem == "W23" or lexem == "W24" and INPUT[i + 1] == "R4":
                OUTPUT.append(lexem)
                continue

            # in
            if lexem == "W25" and INPUT[i + 1] == I.values and INPUT[i - 1] == I.values or INPUT[
                i + 1] == N.values and \
                    INPUT[i - 1] == N.values or INPUT[i + 1] == C.values and INPUT[i - 1] == C.values:
                OUTPUT.append(lexem)
                continue

            # теперь опишу по сути все O
            # всё работатет через огромные сука костыли
            if lexem == "O1" or lexem == "O2" or lexem == "O3" or lexem == "O4" or lexem == "O5" or lexem == "O6" \
                    or lexem == "O7" or lexem == "O8" or lexem == "O9" or lexem == "O10" or lexem == "O11" \
                    and INPUT[i + 1] == I.values or INPUT[i - 1] == I.values and INPUT[i + 1] == N.values \
                    or INPUT[i - 1] == N.values:
                print("зачёл")
                OUTPUT.append(lexem)
                continue

            # .
            if lexem == "R7" and INPUT[i + 1] == I.values or INPUT[i + 1] == W.values:
                OUTPUT.append(lexem)
                continue

            # :
            if lexem == "R8" and INPUT[i + 1] == I.values:
                OUTPUT.append(lexem)
                continue

            # ,
            if lexem == "R6" and INPUT[i + 1] == I.values and INPUT[i - 1] == I.values and INPUT[
                i + 1] == C.values and \
                    INPUT[i - 1] == C.values and INPUT[i + 1] == N.values and INPUT[i - 1] == N.values:
                OUTPUT.append(lexem)
                continue

            # если это табуляция,переход на новую строку,пробел,
            # или константные значения,просто записываем их
            if lexem == "R9" or lexem == "R1" or lexem == "R3" or lexem in I.values() or lexem in \
                    C.values() or lexem in N.values():
                OUTPUT.append(lexem)
                continue

            if lexem == "R2":
                OUTPUT.append(lexem + "\n")
                continue

            # break+continue
            if lexem == "W1" or lexem == "W2":
                OUTPUT.append(lexem)
                continue

            # true+false+null
            if lexem == "W18" or lexem == "W19" or lexem == "W20":
                OUTPUT.append(lexem)
                continue

            # раздел для разделителей
            # ()
            if lexem == "R4":
                STACK.append(lexem)
                OUTPUT.append(lexem)
                continue

            if lexem == "R5":
                if STACK[0] == "R4":
                    STACK.pop()
                    OUTPUT.append(lexem)
                    continue
                else:
                    OUTPUT.append(lexem)
                    number_of_mistakes += 1
                    massiv_of_mistakes.append("Не закрыты скобки")

            # []
            if lexem == "R10":
                STACK.append(lexem)
                OUTPUT.append(lexem)
                continue

            if lexem == "R11":
                if STACK[0] == "R10":
                    STACK.pop()
                    OUTPUT.append(lexem)
                    continue
                else:
                    OUTPUT.append(lexem)
                    number_of_mistakes += 1
                    massiv_of_mistakes.append("Не закрыты скобки")

            # {}
            if lexem == "R12":
                STACK.append(lexem)
                OUTPUT.append(lexem)
                continue

            if lexem == "R13":
                if STACK[0] == "R12":
                    STACK.pop()
                    OUTPUT.append(lexem)
                    continue
                else:
                    OUTPUT.append(lexem)
                    number_of_mistakes += 1
                    massiv_of_mistakes.append("Не закрыты скобки")
        else:

            # если это табуляция,переход на новую строку,пробел,
            # или константные значения,просто записываем их
            if lexem == "R9" or lexem == "R1" or lexem == "R3" or lexem in I.values() or lexem in \
                    C.values() or lexem in N.values():
                OUTPUT.append(lexem)
                continue

            if lexem == "R2":
                OUTPUT.append(lexem + "\n")
                continue

            # break+continue
            if lexem == "1" or lexem == "W2":
                OUTPUT.append(lexem)
                continue

            # true+false+null
            if lexem == "W18" or lexem == "W19" or lexem == "W20":
                OUTPUT.append(lexem)
                continue

            # раздел для разделителей
            # ()
            if lexem == "R4":
                STACK.append(lexem)
                OUTPUT.append(lexem)
                continue

            if lexem == "R5":
                if STACK[0] == "R4":
                    STACK.pop()
                    OUTPUT.append(lexem)
                    continue
                else:
                    OUTPUT.append(lexem)
                    number_of_mistakes += 1
                    massiv_of_mistakes.append("Не закрыты скобки")

            # []
            if lexem == "R10":
                STACK.append(lexem)
                OUTPUT.append(lexem)
                continue

            if lexem == "R11":
                if STACK[0] == "R10":
                    STACK.pop()
                    OUTPUT.append(lexem)
                    continue
                else:
                    OUTPUT.append(lexem)
                    number_of_mistakes += 1
                    massiv_of_mistakes.append("Не закрыты скобки")

            # {}
            if lexem == "R12":
                STACK.append(lexem)
                OUTPUT.append(lexem)
                continue

            if lexem == "R13":
                if STACK[0] == "R12":
                    STACK.pop()
                    OUTPUT.append(lexem)
                    continue
                else:
                    OUTPUT.append(lexem)
                    number_of_mistakes += 1
                    massiv_of_mistakes.append("Не закрыты скобки")

    with open("Лексемы_проверенные.txt", "w") as write_file:
        write_file.write(" ".join(map(str, OUTPUT)))


if __name__ == '__main__':
    main()
