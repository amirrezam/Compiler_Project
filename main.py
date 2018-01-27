# in the name of god

keywords = [
    "public", "class", "static", "void", "main", "extends", "return",
    "if", "else", "while", "for", "true", "false", "boolean", "int"
]

one_char_token = [
    "{", "}", "(", ")", ";", ",", ".", "$"
]

symbol_tables = {
    "package": [],
}

extend_relation = {}

table_stack = ["package"]

extend_stack = []

scope_stack = [0]

prog = ""

current_index = 0

var_declaration = False

number_of_lines = 0


def get_program():
    global prog
    while True:
        s = input()
        if s.find("EOF") != -1:
            break
        prog += s + '\n'
    prog += "$"


def exist(arr, s, e, l):
    for i in range(s, e):
        if arr[i]["name"] == l:
            return i
    return -1

def eliminate_space():
    global current_index
    while prog[current_index].isspace():
        current_index += 1


def search(state, start_index):
    global current_index, number_of_lines

    if state == 0:
        while prog[current_index].isspace():
            start_index += 1
            current_index += 1

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
            if current_char == "{" and table_stack[-1] == "package":
                table_stack.append(extend_stack[-1])
                extend_stack.pop()
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
        elif current_char == "/":
            return search(14, start_index)
        else:
            return ["error", start_index]

    elif state == 1:
        if current_char.isalpha() or current_char.isdigit():
            return search(1, start_index)
        else:
            current_index -= 1
            lexeme = prog[start_index: current_index]
            if lexeme in keywords:
                return ["keywords", lexeme]

            head_table = table_stack[-1]
            if head_table == "package":
                # redefinition error TODO
                if len(extend_stack) == 0:
                    symbol_tables[lexeme] = []
                    extend_stack.append(lexeme)
                else:
                    extend_relation[extend_stack[-1]] = lexeme
                return ["identifier", -1, -1]
            elif var_declaration:
                st = scope_stack[-1]
                en = len(symbol_tables[table_stack[-1]])
                index = exist(symbol_tables[table_stack[-1]], st, en, lexeme)
                if index != -1:
                    print("Redefinition Error ", lexeme, " ", symbol_tables[table_stack[-1]])
                    return ["identifier", index, table_stack[-1]]
                else:
                    symbol_tables[table_stack[-1]].append({"name": lexeme})
                    return ["identifier", len(symbol_tables[table_stack[-1]]) - 1, table_stack[-1]]
            elif lexeme in symbol_tables:
                table_stack.append(lexeme)
                return ["identifier", -1, -1]
            else:
                st = scope_stack[-1]
                en = len(symbol_tables[table_stack[-1]])
                ind0 = exist(symbol_tables[table_stack[-1]], st, en, lexeme)
                if ind0 != -1:
                    return ["identifier", ind0, table_stack[-1]]
                en = st
                st = scope_stack[0]
                ind1 = exist(symbol_tables[table_stack[-1]], st, en, lexeme)
                if ind1 != -1:
                    return ["identifier", ind1, table_stack[-1]]
                current_table = table_stack[-1]
                while current_table in extend_relation:
                    # print(current_table, " inja \n", extend_relation)
                    current_table = extend_relation[current_table]
                    ind = exist(symbol_tables[current_table], 0, len(symbol_tables[current_table]), lexeme)
                    if ind != -1:
                        return ["identifier", ind, current_table]
                print("Error using variable without definition")
                symbol_tables[table_stack[-1]].append({"name": lexeme})
                return ["identifier", len(symbol_tables[table_stack[-1]]) - 1, table_stack[-1]]

    elif state == 3:
        if current_char.isdigit():
            return search(3, start_index)
        else:
            current_index -= 1
            lexeme = prog[start_index: current_index]
            return ["integer", lexeme]

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
    elif state == 14:
        if current_char == "/":
            return search(15, start_index)
        if current_char == "*":
            return search(17, start_index)
        else:
            return ["error", start_index]
    elif state == 15:
        if current_char != "\n":
            return search(15, start_index)
        else:
            number_of_lines += 1
            return search(0, current_index)
    elif state == 17:
        if current_char == "*":
            return search(18, start_index)
        else:
            return search(17, start_index)

    elif state == 18:
        if current_char == "/":
            return search(0, current_index)
        else:
            return search(17, current_index)



def next_token(isdeclaration):
    global current_index, var_declaration
    var_declaration = isdeclaration

    if current_index >= len(prog):
        return [-1, -1] # End of program

    while prog[current_index].isspace():
        current_index += 1

    start_index = current_index

    token = search(0, start_index)
    while token[0] == "error":
        print("Error in index ", start_index, prog[start_index:current_index])
        current_index -= 1
        start_index = current_index
        token = search(0, start_index)
    return (token, start_index)

