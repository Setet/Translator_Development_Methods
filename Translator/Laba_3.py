import json

with open("I.json", "r", encoding="utf-8") as read_file:
    I = json.load(read_file)

with open("C.json", "r", encoding="utf-8") as read_file:
    C = json.load(read_file)

with open("N.json", "r", encoding="utf-8") as read_file:
    N = json.load(read_file)

with open("W.json", "r", encoding="utf-8") as read_file:
    W = json.load(read_file)

with open("O.json", "r", encoding="utf-8") as read_file:
    O = json.load(read_file)

with open("R.json", "r", encoding="utf-8") as read_file:
    R = json.load(read_file)

with open("Лексемы_ОПН.txt", "r") as read_file:
    INPUT = read_file.read().split()

STACK = []
OUTPUT = []


class Function:
    def __init__(self, name, type, point):
        self.name = name
        self.type = type
        self.point = point


functions = []
func_stack = []


def wrap(string, m=""):
    return m.ljust(5, " ") + string.strip() + "\n"


for i in range(len(INPUT)):
    lexem = INPUT[i]

    if lexem in O.values():
        for key, value in O.items():
            if value == lexem:
                if lexem == "O6":
                    id = STACK.pop()
                    STACK.append(wrap(f"{id} = {id} + 1"))
                elif lexem == "O8":
                    id = STACK.pop()
                    STACK.append(wrap(f"{id} = {id} - 1"))
                elif lexem == "O11":
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(f"{id1} < {id2}")
                elif lexem == "O13":
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(f"{id1} > {id2}")
                elif lexem == "O2":
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(f"{id1} == {id2}")
                elif lexem == "O16":
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(f"{id1} != {id2}")
                elif lexem == "O12":
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(f"{id1} <= {id2}")
                elif lexem == "O14":
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(f"{id1} >= {id2}")
                elif lexem == "O1":
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(wrap(f"{id1} {key} {id2}"))
                else:
                    id2 = STACK.pop()
                    id1 = STACK.pop()
                    STACK.append(f"{id1} {key} {id2}")

    elif lexem in I.values():
        for key, value in I.items():
            if value == lexem:
                STACK.append(key)

    elif lexem in C.values():
        for key, value in C.items():
            if value == lexem:
                STACK.append(key)

    elif lexem in N.values():
        for key, value in N.items():
            if value == lexem:
                STACK.append(key)


    elif lexem == "Ф":
        n = int(STACK.pop())
        params = STACK[-n:]
        del STACK[-n:]
        if (func := list(filter(lambda function: function.name == params[0], functions))) and func[
            0].type == "function":
            STACK.append(wrap(f"{params[0]}({','.join(map(str.strip, params[1:]))})"))
        else:
            STACK.append(wrap(f"{params[0]}({','.join(map(str.strip, params[1:]))})"))


    elif lexem == "АЭМ":
        n = int(STACK.pop())
        params = STACK[-n:]
        del STACK[-n:]
        STACK.append(f"{params[0]}{''.join(map(lambda x: '[' + str(x) + ']', params[1:]))}")

    elif lexem == "MASS":
        n = int(STACK.pop())
        params = STACK[-n:]
        del STACK[-n:]
        STACK.append(wrap(f"{params[1]}, dimension ({','.join(params[2:])}) :: {params[0]}"))

    elif lexem == "W9":
        func = functions[-1]
        STACK[func.point] = STACK[func.point].replace("subroutine", "function")
        func.type = "function"
        STACK.append(wrap(f"{func.name} = {STACK.pop()}"))

    elif lexem == "W6":
        m = STACK.pop()
        exp = STACK.pop()
        STACK.append(wrap(f"if (.not. ({exp})) break {m}"))

    elif lexem == "W1":
        STACK.append(wrap(f"break {STACK.pop()}"))

    elif lexem == ":":
        m = STACK.pop()
        op = STACK.pop()
        STACK.append(wrap(op, m))

    elif lexem == "W8":
        STACK.append(wrap(f"while({STACK.pop()})"))

    elif lexem == "W4":
        params = STACK[-3:]
        del STACK[-3:]
        STACK.append(params[0])
        STACK.append(wrap(f"for({params[1]})"))
        step = params[2]

    elif lexem == "R2":
        STACK.append("\n")

    else:
        STACK.append(lexem)

with open("Эксперементальный_код_из_ОПН.txt", "w", encoding="utf-8") as write_file:
    OUTPUT.extend(STACK)
    write_file.write("".join(OUTPUT))
