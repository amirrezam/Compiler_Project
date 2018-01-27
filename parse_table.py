grammer = [
    ("",""),
    ("Goal", "Source EOF"), # 1
    ("Source", "ClassDeclarations MainClass"), # 2
    ("MainClass", "#JMP_FIRST public class Identifier { public static void main ( ) { #START_SCOPE VarDeclarations Statements #END_SCOPE } } #POP_SYMBOL_TABLE"), # 3
    ("ClassDeclarations", "ClassDeclaration ClassDeclarations"), # 4
    ("ClassDeclaration", "class Identifier Extension { FieldDeclarations MethodDeclarations } #POP_SYMBOL_TABLE"), # 5
    ("Extension", "extends Identifier"), # 6
    ("Extension", ""), # 7
    ("FieldDeclarations", ""), # 8
    ("FieldDeclarations", "FieldDeclaration FieldDeclarations"), # 9
    ("FieldDeclaration", "#SET_DECLARATION static Type #ID_ADDRESS Identifier #RESET_DECLARATION ;"), # 10
    ("VarDeclarations", "VarDeclaration VarDeclarations"), # 11
    ("VarDeclarations", ""), # 12
    ("VarDeclaration", "#SET_DECLARATION Type #ID_ADDRESS Identifier #RESET_DECLARATION ;"), # 13
    ("MethodDeclarations", "MethodDeclaration MethodDeclarations"), # 14
    ("MethodDeclarations", ""), # 15
    ("MethodDeclaration", "#SET_DECLARATION public static Type #DEFINE_FUNC Identifier #RESET_DECLARATION #START_SCOPE ( Parameters ) #END_FUNC { VarDeclarations Statements return GenExpression ; #END_SCOPE #JMP_RETURN }"), # 16
    ("Parameters", "#SET_DECLARATION Type #ID_ADDRESS Identifier #RESET_DECLARATION Parameter"), # 17
    ("Parameters", ""), # 18
    ("Parameter", "#SET_DECLARATION , Type #ID_ADDRESS Identifier #RESET_DECLARATION Parameter"), # 19
    ("Parameter", ""), # 20
    ("Type", "boolean"), # 21
    ("Type", "int"), # 22
    ("Statements", "A"), # 23
    ("A", "Statement A"), # 24
    ("A",""), # 25
    ("Statement","{ Statements }"), # 26
    ("Statement","if ( GenExpression ) #SAVE Statement else #JPF_SAVE Statement #JP"), # 27
    ("Statement","while #LABEL ( GenExpression ) #SAVE Statement #WHILE"), # 28
    ("Statement","for ( Identifier = Integer ; RelTerm ; Identifier += Integer ) Statement"), # 29
    ("Statement","#PID Identifier = GenExpression #ASSIGN ;"), # 30
    ("Statement","System.out.println ( GenExpression #PRINT ) ;"), # 31
    ("GenExpression","Expression I"), # 32
    ("I",""), # 33
    ("I","G H"), # 34
    ("Expression","Term C"), # 35
    ("C","B C"), # 36
    ("C",""), # 37
    ("B","+ Term #ADD"), # 38
    ("B","- Term #SUB"), # 39
    ("Term","Factor D"), # 40
    ("D","* Factor #MULT D"), # 41
    ("D",""), # 42
    ("Factor","( Expression )"), # 43
    ("Factor","#PUSH_BOOL true"), # 44
    ("Factor","#PUSH_BOOL false"), # 45
    ("Factor","Integer"), # 46
    ("Factor","#PID_CLASS Identifier E"), # 47
    ("E",""), # 48
    ("E",". #PID_METHOD Identifier #POP_SYMBOL_TABLE F"), # 49
    ("F",""), # 50
    ("F","( Arguments ) #JMP_RETURN_ADDRESS"), # 51
    ("RelExpression","RelTerm H"), # 52
    ("H","&& RelTerm H"), # 53
    ("H",""), # 54
    ("RelTerm","Expression G"), # 55
    ("G","== Expression #EQUALITY"), # 56
    ("G","< Expression #LESS_THAN"), # 57
    ("Arguments","GenExpression Argument"), # 58
    ("Arguments",""), # 59
    ("Argument",""), # 60
    ("Argument",", GenExpression Argument"), # 61
    ("Identifier","identifier"), # 62
    ("Integer","#PUSH_INT integer"), # 63
    ("ClassDeclarations", ""), # 64
]

parse_table = {
    "VarDeclarations": {
        "(": 12,
        "a": 12,
        "b": 11,
        "d": 12,
        "f": 12,
        "i": 11,
        "n": 12,
        "o": 12,
        "t": 12,
        "w": 12,
        "y": 12,
        "{": 12,
        "}": 12,
        "r": 12,
    },
    "Statements": {
        "d": 23,
        "f": 23,
        "o": 23,
        "w": 23,
        "y": 23,
        "{": 23,
        "}": 23,
        "r": 23,
    },
    "MethodDeclarations": {
        "p": 14,
        "}": 15,
    },
    "Type": {
        "b": 21,
        "i": 22,
    },
    "Parameters": {
        ")": 18,
        "b": 17,
        "i": 17,
    },
    "GenExpression": {
        "(": 32,
        "a": 32,
        "d": 32,
        "n": 32,
        "t": 32,
    },
    "Parameter": {
        ")": 20,
        ",": 19,
    },
    "A": {
        "d": 24,
        "f": 24,
        "o": 24,
        "w": 24,
        "y": 24,
        "{": 24,
        "}": 25,
        "r": 25,
    },
    "Statement": {
        "d": 30,
        "f": 27,
        "o": 29,
        "w": 28,
        "y": 31,
        "{": 26,
    },
    "RelTerm": {
        "(": 55,
        "a": 55,
        "d": 55,
        "n": 55,
        "t": 55,
    },
    "Expression": {
        "(": 35,
        "a": 35,
        "d": 35,
        "n": 35,
        "t": 35,
    },
    "I": {
        ")": 33,
        ",": 33,
        ";": 33,
        "<": 34,
        "^": 34,
    },
    "G": {
        "<": 57,
        "^": 56,
    },
    "H": {
        "&": 53,
        ")": 54,
        ",": 54,
        ";": 54,
    },
    "Term": {
        "(": 40,
        "a": 40,
        "d": 40,
        "n": 40,
        "t": 40,
    },
    "B": {
        "+": 38,
        "-": 39,
    },
    "C": {
        "&": 37,
        ")": 37,
        "+": 36,
        ",": 37,
        "-": 36,
        ";": 37,
        "<": 37,
        "^": 37,
    },
    "D": {
        "&": 42,
        ")": 42,
        "+": 42,
        ",": 42,
        "-": 42,
        ";": 42,
        "<": 42,
        "^": 42,
        "*": 41,
    },
    "Factor": {
        "(": 43,
        "a": 45,
        "d": 47,
        "n": 46,
        "t": 44,
    },
    "Arguments": {
        "(": 58,
        "a": 58,
        "d": 58,
        "n": 58,
        "t": 58,
        ")": 59,
    },
    "Argument": {
        ")": 60,
        ",": 61,
    },
    "E": {
        "&": 48,
        ")": 48,
        "*": 48,
        "+": 48,
        ",": 48,
        "-": 48,
        ".": 49,
        ";": 48,
        "<": 48,
        "^": 48,
    },
    "F": {
        "&": 50,
        ")": 50,
        "*": 50,
        "+": 50,
        ",": 50,
        "-": 50,
        ";": 50,
        "<": 50,
        "^": 50,
        "(": 51,
    },
    "Identifier": {
        "d": 62,
    },
    "Integer": {
        "n": 63,
    },
    "RelExpression": {
        "(": 52,
        "a": 52,
        "d": 52,
        "n": 52,
        "t": 52,
    },
    "FieldDeclaration": {
        "s": 10,
    },
    "Goal": {
        "c": 1,
        "p": 1,
    },
    "MethodDeclaration": {
        "p": 16,
    },
    "ClassDeclarations": {
        "c": 4,
        "p": 64,
    },
    "MainClass": {
        "p": 3,
    },
    "Source": {
        "c": 2,
        "p": 2,
    },
    "FieldDeclarations": {
        "p": 8,
        "s": 9,
        "}": 8,
    },
    "ClassDeclaration": {
        "c": 5,
    },
    "VarDeclaration": {
        "b": 13,
        "i": 13,
    },
    "Extension": {
        "x": 6,
        "{": 7,
    },
}

map_terminals = {
    "==": "^",
    "&&": "&",
    "+=": "%",
    "false": "a",
    "boolean": "b",
    "class": "c",
    "identifier": "d",
    "EOF": "e",
    "if": "f",
    "int": "i",
    "else": "l",
    "main": "m",
    "integer": "n",
    "for": "o",
    "public": "p",
    "return": "r",
    "static": "s",
    "true": "t",
    "void": "v",
    "while": "w",
    "extends": "x",
    "System.out.println": "y",
    "{": "{",
    "}": "}",
    "(": "(",
    ",": ",",
    ";": ";",
    ".": ".",
    "+": "+",
    "-": "-",
    "*": "*",
    "<": "<",
    ")": ")",
    "=": "=",
}

follows = {
    "VarDeclarations": ["r", "d", "f", "w", "y", "{", "}", "o"],
    "Statements": ["r", "}"],
    "MethodDeclarations": ["}"],
    "Type": ["d"],
    "Parameters": [")"],
    "GenExpression": [")", ";", ","],
    "Parameter": [")"],
    "A": ["r", "}"],
    "Statement": ["r", "d", "f", "w", "y", "{", "l", "}", "o"],
    "RelTerm": ["&", ")", ";", ","],
    "Expression": ["&", ")", ";", "<", ",", "^"],
    "I": [")", ";", ","],
    "G": ["&", ")", ";", ","],
    "H": [")", ";", ","],
    "Term": ["&", ")", ";", "+", "<", ",", "-", "^"],
    "B": ["&", ")", ";", "+", "<", ",", "-", "^"],
    "C": ["&", ")", ";", "<", ",", "^"],
    "D": ["&", ")", ";", "+", "<", ",", "-", "^"],
    "Factor": ["&", ")", ";", "+", "<", ",", "-", "^", "*"],
    "Arguments": [")"],
    "Argument": [")"],
    "E": ["&", ")", ";", "+", "<", ",", "-", "^", "*"],
    "F": ["&", ")", ";", "+", "<", ",", "-", "^", "*"],
    "Identifier": ["%", "&", "(", ")", "*", "+", ",", "-", ".", "x", "{", ";", "<", "=", "^"],
    "Integer": ["&", ")", ";", "+", "<", ",", "-", "^", "*"],
    "RelExpression": [],
    "FieldDeclaration": ["p", "s", "}"],
    "Goal": ["$"],
    "MethodDeclaration": ["p", "}"],
    "ClassDeclarations": ["p"],
    "MainClass": ["e"],
    "Source": ["e"],
    "FieldDeclarations": ["p", "}"],
    "ClassDeclaration": ["p", "c"],
    "VarDeclaration": ["b", "r", "d", "f", "w", "y", "i", "{", "}", "o"],
    "Extension": ["{"],
}

terminals = list(map_terminals.keys())