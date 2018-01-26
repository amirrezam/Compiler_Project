# in the name of god

keywords = [
    "public", "class", "static", "void", "main", "extends", "return",
    "if", "else", "while", "for", "true", "false", "boolean", "int"
]

one_char_token = [
    "{", "}", "(", ")", ";", ",", ".", "$"
]

prog = ""
current_index = 0


def get_program():
    global prog
    while True:
        s = input()
        if s.find("EOF") != -1:
            break
        prog += s + '\n'
    prog += "$"


def search(state, start_index):
    global current_index
    if (current_index + 18) < len(prog) and prog[current_index: current_index + 18] == "System.out.println":
        current_index += 18
        return ["keyword", "System.out.println"]

    current_char = prog[current_index]
    current_index += 1

    if state == 0:
        if current_char == "*":
            return ["OP", "*"]
        if current_char == "<":
            return ["RELOP", "<"]
        if current_char == "$":
            return ["$", "$"]
        if current_char in one_char_token:
            return [current_char, current_char]
        if current_char.isalpha():
            return search(1, start_index)
        elif current_char.isdigit():
            return search(3, start_index)
        elif current_char == "+":
            return search(5, start_index)
        elif current_char == "-":
            return search(8, start_index)
        elif current_char == "=":
            return search(10, start_index)
        elif current_char == "&":
            return search(13, start_index)
        else:
            print("inja error", current_char, current_index)
            return ["error", start_index]

    elif state == 1:
        if current_char.isalpha() or current_char.isdigit():
            return search(1, start_index)
        else:
            current_index -= 1
            if prog[start_index: current_index] in keywords:
                return ["keywords", prog[start_index: current_index]]
            return ["identifier", -1] # symbol table

    elif state == 3:
        if current_char.isdigit():
            return search(3, start_index)
        else:
            current_index -= 1
            return ["integer", "integer"]

    elif state == 5:
        if current_char.isdigit():
            return search(3, start_index)
        elif current_char == "=":
            return ["OP", "+="]
        else:
            current_index -= 1
            return ["OP", "+"]

    elif state == 8:
        if current_char.isdigit():
            return search(3, start_index)
        else:
            current_index -= 1
            return ["OP", "-"]

    elif state == 10:
        if current_char == "=":
            return ["RELOP", "=="]
        else:
            current_index -= 1
            return ["OP", "="]

    elif state == 13:
        if current_char == "&":
            return ["OP", "&&"]
        else:
            return ["error", start_index]


def next_token():
    global current_index

    if current_index >= len(prog):
        return [-1, -1] # End of program

    while prog[current_index].isspace():
        current_index += 1

    start_index = current_index
    while search(0, start_index)[0] == "error":
        print("Error in index ", start_index, prog[start_index], ord(' '), " ",  ord(prog[start_index]), " ", prog[start_index].isspace())
        start_index += 1
        current_index = start_index
    current_index = start_index

    token = search(0, start_index)
    return (token, start_index)

