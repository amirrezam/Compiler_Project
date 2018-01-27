# LL1 parser

from parse_table import parse_table, grammer, map_terminals, terminals, follows
from main import next_token, get_program, symbol_tables, table_stack, scope_stack
import sys

var_declaration = False

get_program()
parse_stack = []
parse_stack.append("Goal")

start_index = 0
prev_number_line = 0
number_of_lines = 0

return_value_counter = 2000
return_address_counter = 3000
var_counter = 1000
temp_counter = 4000

complete_token = []

semantic_stack = []

PB = [""]


def get_temp():
    global temp_counter
    temp_counter += 4
    return temp_counter - 4


def pop_stack(k):
    while len(symbol_tables[table_stack[-1]]) > k:
        symbol_tables[table_stack[-1]].pop()


def jp(L):
    return "(JP, {}, , )".format(L)


def assign(S, D):
    return "(ASSIGN, {}, {}, )".format(S, D)


def add(S1, S2, D):
    return "(ADD, {}, {}, {})".format(S1, S2, D)


def mult(S1, S2, D):
    return "(MULT, {}, {}, {})".format(S1, S2, D)


def sub(S1, S2, D):
    return "(SUB, {}, {}, {})".format(S1, S2, D)


def equality(S1, S2, D):
    return "(EQ, {}, {}, {})".format(S1, S2, D)


def less(S1, S2, D):
    return "(LT, {}, {}, {})".format(S1, S2, D)


def jpf(S, D):
    return "(JPF, {}, {}, )".format(S, D)


def andd(S1, S2, D):
    return "(AND, {}, {}, {})".format(S1, S2, D)


def print_assemble(S):
    return "(PRINT, {}, , )".format(S)


def exist_var(a):
    if not ("type" in a):
        print("Error, Var {} doesn't have type in line {}".format(a["name"], number_of_lines))
        sys.exit()


def handle_action(action):
    global return_value_counter, var_counter, semantic_stack, return_address_counter, var_declaration
    if action == "POP_SYMBOL_TABLE":
        table_stack.pop()
    elif action == "START_SCOPE":
        scope_stack.append(len(symbol_tables[table_stack[-1]]))
    elif action == "END_SCOPE":
        pop_stack(scope_stack[-1])
        scope_stack.pop()
    elif action == "SET_DECLARATION":
        var_declaration = True
    elif action == "RESET_DECLARATION":
        var_declaration = False
    elif action == "PUSH_INT":
        semantic_stack.append(("#{}".format(complete_token[1]), "int"))  #(complete_token[1], "int")
    elif action == "PUSH_BOOL":
        semantic_stack.append((complete_token[1], "boolean"))  #(complete_token[1], "bool")
    elif action == "DEFINE_FUNC":
        type = semantic_stack[-1]
        semantic_stack.pop()
        ind = complete_token[1]
        semantic_stack.append(ind)
        symbol_tables[table_stack[-1]][ind]["return_address"] = return_address_counter
        return_address_counter += 4
        symbol_tables[table_stack[-1]][ind]["return_value"] = return_value_counter
        return_value_counter += 4
        symbol_tables[table_stack[-1]][ind]["prog_start"] = len(PB)
        symbol_tables[table_stack[-1]][ind]["param_start"] = var_counter
        symbol_tables[table_stack[-1]][ind]["type"] = type
    elif action == "END_FUNC":
        ind = semantic_stack[-1]
        symbol_tables[table_stack[-1]][ind]["param_end"] = var_counter
    elif action == "ADD_TYPE":
        type = complete_token[1]
        semantic_stack.append(type)
    elif action == "ID_ADDRESS":
        ind = complete_token[1]
        type = semantic_stack[-1]
        semantic_stack.pop()
        symbol_tables[table_stack[-1]][ind]["address"] = var_counter
        symbol_tables[table_stack[-1]][ind]["type"] = type
        var_counter += 4
    elif action == "JMP_RETURN":
        ind = semantic_stack[-2]
        val = semantic_stack[-1][0]
        type = semantic_stack[-1][1]
        semantic_stack.pop()
        semantic_stack.pop()
        exist_var(symbol_tables[table_stack[-1]][ind])
        func_type = symbol_tables[table_stack[-1]][ind]["type"]
        if type != func_type:
            print("Error Type Checking in return value function {}".format(symbol_tables[table_stack[-1]][ind]["name"]))
            sys.exit()
        PB.append(assign(val, symbol_tables[table_stack[-1]][ind]["return_value"]))
        PB.append(jp("@{}".format(symbol_tables[table_stack[-1]][ind]["return_address"])))
    elif action == "JMP_FIRST":
        PB[0] = jp("{}".format(len(PB)))
    elif action == "ADD":
        t = get_temp()
        a = semantic_stack[-1][0]
        b = semantic_stack[-2][0]
        type_a = semantic_stack[-1][1]
        type_b = semantic_stack[-2][1]
        if type_a != type_b:
            print("Error Type Checking in ADD in line {}".format(prev_number_line))
            sys.exit()
        PB.append(add(a, b, t))
        semantic_stack.pop()
        semantic_stack.pop()
        semantic_stack.append((t, type_a))
    elif action == "MULT":
        t = get_temp()
        a = semantic_stack[-1][0]
        b = semantic_stack[-2][0]
        type_a = semantic_stack[-1][1]
        type_b = semantic_stack[-2][1]
        if type_a != type_b:
            print("Error Type Checking in MULT in line {}".format(prev_number_line))
            sys.exit()
        PB.append(mult(a, b, t))
        semantic_stack.pop()
        semantic_stack.pop()
        semantic_stack.append((t, type_a))
    elif action == "SUB":
        t = get_temp()
        a = semantic_stack[-1][0]
        b = semantic_stack[-2][0]
        type_a = semantic_stack[-1][1]
        type_b = semantic_stack[-2][1]
        if type_a != type_b:
            print("Error Type Checking in SUB in line {}".format(prev_number_line))
            sys.exit()
        PB.append(sub(b, a, t))
        semantic_stack.pop()
        semantic_stack.pop()
        semantic_stack.append((t,type_a))
    elif action == "PID_CLASS":
        t = complete_token
        ind = t[1]
        if ind != -1:
            exist_var(symbol_tables[table_stack[-1]][ind])
            semantic_stack.append((symbol_tables[table_stack[-1]][ind]["address"], symbol_tables[table_stack[-1]][ind]["type"]))
    elif action == "PID_METHOD":
        t = complete_token
        ind = t[1]
        exist_var(symbol_tables[t[2]][ind])
        if "address" in symbol_tables[t[2]][ind]:
            semantic_stack.append((symbol_tables[t[2]][ind]["address"], symbol_tables[t[2]][ind]["type"]))
        else:
            semantic_stack.append((symbol_tables[t[2]][ind]["return_value"], symbol_tables[t[2]][ind]["type"]))
            semantic_stack.append(symbol_tables[t[2]][ind]["prog_start"])
            semantic_stack.append(symbol_tables[t[2]][ind]["return_address"])
            semantic_stack.append(symbol_tables[t[2]][ind]["param_end"])
            semantic_stack.append(symbol_tables[t[2]][ind]["param_start"])

    elif action == "JMP_RETURN_ADDRESS":
        l = len(PB)
        R_A = semantic_stack[-1]
        P_S = semantic_stack[-2]
        semantic_stack.pop()
        semantic_stack.pop()
        PB.append(assign("#{}".format(l + 2), R_A))
        PB.append(jp(P_S))

    elif action == "EQUALITY":
        t = get_temp()
        a = semantic_stack[-1][0]
        b = semantic_stack[-2][0]
        type_a = semantic_stack[-1][1]
        type_b = semantic_stack[-2][1]
        if type_a != type_b:
            print("Error Type Checking Equality in line {}".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()
        PB.append(equality(a, b, t))
        semantic_stack.append((t,"boolean"))

    elif action == "LESS_THAN":
        t = get_temp()
        a = semantic_stack[-1][0]
        b = semantic_stack[-2][0]
        type_a = semantic_stack[-1][1]
        type_b = semantic_stack[-2][1]
        if type_a != type_b:
            print("Error Type Checking Less than in line {}".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()
        PB.append(less(b, a, t))
        semantic_stack.append((t,"boolean"))

    elif action == "AND_TERM":
        t = get_temp()
        a = semantic_stack[-1][0]
        b = semantic_stack[-2][0]
        type_a = semantic_stack[-1][1]
        type_b = semantic_stack[-2][1]
        if type_a != "boolean" or type_b != "boolean":
            print("Error Type Checking and in line {}, expressions must be boolean".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()
        PB.append(andd(a, b, t))
        semantic_stack.append((t,"boolean"))
    elif action == "LABEL":
        semantic_stack.append(len(PB))

    elif action == "SAVE":
        semantic_stack.append(len(PB))
        PB.append("")

    elif action == "WHILE":
        ind = semantic_stack[-1]
        exp = semantic_stack[-2][0]
        type_exp = semantic_stack[-2][1]
        st = semantic_stack[-3]
        l = len(PB)
        if type_exp != "boolean":
            print("Error Type Checking, Expression must be boolean in line {}".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()
        semantic_stack.pop()
        PB[ind] = jpf(exp, l + 1)
        PB.append(jp(st))

    elif action == "JPF_SAVE":
        ind = semantic_stack[-1]
        exp = semantic_stack[-2][0]
        type_exp = semantic_stack[-2][1]
        l = len(PB)
        if type_exp != "boolean":
            print("Error Type Checking, Expression must be boolean in line {}".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()
        PB[ind] = jpf(exp, l + 1)
        semantic_stack.append(l)
        PB.append("")

    elif action == "JP":
        l = len(PB)
        ind = semantic_stack[-1]
        semantic_stack.pop()
        PB[ind] = jp(l)

    elif action == "PID":
        t = complete_token
        ind = t[1]
        exist_var(symbol_tables[table_stack[-1]][ind])
        semantic_stack.append((symbol_tables[table_stack[-1]][ind]["address"], symbol_tables[table_stack[-1]][ind]["type"]))

    elif action == "ASSIGN":
        s = semantic_stack[-1][0]
        d = semantic_stack[-2][0]
        type_s = semantic_stack[-1][1]
        type_d = semantic_stack[-2][1]
        if type_s != type_d:
            print("Error Type Checking in assignment in line {}".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()
        PB.append(assign(s, d))

    elif action == "PRINT":
        exp = semantic_stack[-1][0]
        type_exp = semantic_stack[-1][1]
        if type_exp != "int":
            print("Error in line {}, Only print integer value".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        PB.append(print_assemble(exp))

    elif action == "FOR":
        a = semantic_stack[-1][0]
        b = semantic_stack[-2][0]
        type_a = semantic_stack[-1][1]
        type_b = semantic_stack[-2][1]
        ind = semantic_stack[-3]
        label = semantic_stack[-5]
        exp = semantic_stack[-4][0]
        type_exp = semantic_stack[-4][1]
        if type_exp != "boolean":
            print("Error Type Checking, Expression must be boolean in line {}".format(prev_number_line))
            sys.exit()
        if type_a != type_b:
            print("Error Type Checking in assignment in line {}".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()
        semantic_stack.pop()
        semantic_stack.pop()
        semantic_stack.pop()
        PB.append(add(a, b, b))
        PB.append(jp(label))
        l = len(PB)
        PB[ind] = jpf(exp, l)

    elif action == "POP_PARAMS":
        current_param = semantic_stack[-1]
        end_param = semantic_stack[-2]
        if current_param != end_param:
            print("Error in call function in line {}, # of arguments don't equal # of parameters".format(prev_number_line))
            sys.exit()
        semantic_stack.pop()
        semantic_stack.pop()

    elif action == "ASSIGN_ARG":
        exp = semantic_stack[-1][0]
        current_param = semantic_stack[-2]
        param_end = semantic_stack[-3]
        if current_param == param_end:
            print("Error in call function in line {}, # of arguments don't equal # of parameters".format(prev_number_line))
            sys.exit()
        else:
            PB.append(assign(exp, current_param))
            semantic_stack[-2] = current_param + 4
            semantic_stack.pop()
    else:
        print("ERROR IN ACTION TYPE")


def get_token():
    global start_index, number_of_lines, complete_token, prev_number_line
    t = next_token(var_declaration)
    # print(t, " token \n\n", "symbol_table: ", symbol_tables, "\n\n", "table_stack: ", table_stack, "\n\n", "scope_stack:", scope_stack, "\n\n", "\n\n\n\n\n\n")
    start_index = t[1]
    prev_number_line = number_of_lines
    number_of_lines = t[2]
    n_token = t[0]
    complete_token = n_token
    if n_token[0] == "identifier" or n_token[0] == "integer":
        token = n_token[0]
    else:
        token = n_token[1]
    return token


token = get_token()


while True:
    if len(parse_stack) == 0:
        print("Empty Parser Stack in Panic")
        sys.exit()
    top = parse_stack[-1]

    # print("\n\n\n token : ", token, "\t\t top: ", top)

    if top.find("#") != -1:
        handle_action(top[1:])
        parse_stack.pop()
        continue
    if top in terminals:
        if top == token:
            if token == "EOF":
                # print("ACCEPT")
                break
            parse_stack.pop()
            token = get_token()
        else:
            print("Error in line {}, expected {} ".format(prev_number_line, top))
            parse_stack.pop()
    else:
        if map_terminals[token] in parse_table[top]:
            parse_stack.pop()
            grm = grammer[parse_table[top][map_terminals[token]]][1].split()
            for i in range(len(grm), 0, -1):
                parse_stack.append(grm[i - 1])
            # print(grammer[parse_table[top][map_terminals[token]]], " Parser Output")
        else:
            error_location = prev_number_line
            token = get_token()
            print("Error in line {}, expected {}".format(error_location, top))
            while not (map_terminals[token] in parse_table[top]):
                if map_terminals[token] in follows[top]:
                    print("Error in line {}, expected {}".format(error_location, top))
                    parse_stack.pop()
                else:
                    token = get_token()

for i in range(len(PB)):
    print("{}\t".format(i), PB[i])

# print(semantic_stack)