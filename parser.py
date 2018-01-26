# LL1 parser

from parse_table import parse_table, grammer, map_terminals, terminals, follows
from main import next_token, keywords, get_program, current_index

get_program()
parse_stack = []
parse_stack.append("Goal")

start_index = 0


def get_token():
    global start_index
    t = next_token()
    start_index = t[1]
    n_token = t[0]
    if n_token[0] == "identifier":
        token = n_token[0]
    else:
        token = n_token[1]
    if token == "$":
        return "EOF"
    return token


token = get_token()


while True:
    if len(parse_stack) == 0:
        print("BE FANA")
        # TODO
    top = parse_stack[-1]
    # print("\n\n\n token : ", token, "\t\t top: ", top)
    # print(parse_stack, " PARSE STACK")
    if top in terminals:
        if top == token:
            if token == "EOF":
                print("ACCEPT")
                break
            parse_stack.pop()
            token = get_token()
        else:
            print("Error at location {} , expected {} ".format(start_index, top))
            parse_stack.pop()
    else:
        if map_terminals[token] in parse_table[top]:
            parse_stack.pop()
            grm = grammer[parse_table[top][map_terminals[token]]][1].split()
            for i in range(len(grm), 0, -1):
                parse_stack.append(grm[i - 1])
            # print(grammer[parse_table[top][map_terminals[token]]], " Parser Output")
        else:
            error_location = start_index
            token = get_token()
            print("Error ar location {} expected {}".format(error_location, top))
            while not (map_terminals[token] in parse_table[top]):
                if map_terminals[token] in follows[top]:
                    print("Error ar location {} expected {}".format(error_location, top))
                    parse_stack.pop()
                else:
                    token = get_token()

