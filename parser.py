# LL1 parser

from parse_table import parse_table, grammer, map_terminals, terminals
from main import next_token, keywords, get_program, current_index

get_program()

parse_stack = []
parse_stack.append("Goal")

# for i in range(100):
#     print(next_token())
print(terminals)

def get_token():
    n_token = next_token()
    if n_token[0] == "identifier":
        token = n_token[0]
    else:
        token = n_token[1]
    if token == "$":
        return "EOF"
    return token


token = get_token()


while True:
    top = parse_stack[-1]
    print("\n\n\n token : ", token, "\t\t top: ", top)
    print(parse_stack, " PARSE STACK")
    if top in terminals :
        if top == token :
            if token == "EOF":
                print("ACCEPT")
                break
            parse_stack.pop()
            token = get_token()

    else:
        if map_terminals[token] in parse_table[top] :
            parse_stack.pop()
            grm = grammer[parse_table[top][map_terminals[token]]][1].split()
            for i in range(len(grm), 0, -1):
                parse_stack.append(grm[i - 1])
            print(grammer[parse_table[top][map_terminals[token]]], " Parser Output")
        else:
            print("ERROR", )
            break
