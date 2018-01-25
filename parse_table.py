
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

grammer = [
    ("",""),
    ("Goal", "Source EOF"), # 1
    ("Source", "ClassDeclarations MainClass"), # 2
    ("MainClass", "public class Identifier { public static void main ( ) { VarDeclarations Statements } }"), # 3
    ("ClassDeclarations", "ClassDeclaration ClassDeclarations"), # 4
    ("ClassDeclaration", "class Identifier Extension { FieldDeclarations MethodDeclarations }"), # 5
    ("Extension", "extends Identifier"), # 6
    ("Extension", ""), # 7
    ("FieldDeclarations", ""), # 8
    ("FieldDeclarations", "FieldDeclaration FieldDeclarations"), # 9
    ("FieldDeclaration", "static Type Identifier ;"), # 10
    ("VarDeclarations", "VarDeclaration VarDeclarations"), # 11
    ("VarDeclarations", ""), # 12
    ("VarDeclaration", "Type Identifier ;"), # 13
    ("MethodDeclarations", "MethodDeclaration MethodDeclarations"), # 14
    ("MethodDeclarations", ""), # 15
    ("MethodDeclaration", "public static Type Identifier ( Parameters ) { VarDeclarations Statements return GenExpression ; }"), # 16
    ("Parameters", "Type Identifier Parameter"), # 17
    ("Parameters", ""), # 18
    ("Parameter", ", Type Identifier Parameter"), # 19
    ("Parameter", ""), # 20
    ("Type", "boolean"), # 21
    ("Type", "int"), # 22
    ("Statements", "A"), # 23
    ("A", "Statement A"), # 24
    ("A",""), # 25
    ("Statement","{ Statements }"), # 26
    ("Statement","if ( GenExpression ) Statement else Statement"), # 27
    ("Statement","while ( GenExpression ) Statement"), # 28
    ("Statement","for ( Identifier = Integer ; RelTerm ; Identifier += Integer ) Statement"), # 29
    ("Statement","Identifier = GenExpression ;"), # 30
    ("Statement","System.out.println ( GenExpression ) ;"), # 31
    ("GenExpression","Expression I"), # 32
    ("I",""), # 33
    ("I","G H"), # 34
    ("Expression","Term C"), # 35
    ("C","B C"), # 36
    ("C",""), # 37
    ("B","+ Term"), # 38
    ("B","- Term"), # 39
    ("Term","Factor D"), # 40
    ("D","* Factor D"), # 41
    ("D",""), # 42
    ("Factor","( Expression )"), # 43
    ("Factor","true"), # 44
    ("Factor","false"), # 45
    ("Factor","Integer"), # 46
    ("Factor","Identifier E"), # 47
    ("E",""), # 48
    ("E",". Identifier F"), # 49
    ("F",""), # 50
    ("F","( Arguments )"), # 51
    ("RelExpression","RelTerm H"), # 52
    ("H","&& RelTerm H"), # 53
    ("H",""), # 54
    ("RelTerm","Expression G"), # 55
    ("G","== Expression"), # 56
    ("G","< Expression"), # 57
    ("Arguments","GenExpression Argument"), # 58
    ("Arguments",""), # 59
    ("Argument",""), # 60
    ("Argument",", GenExpression Argument"), # 61
    ("Identifier","identifier"), # 62
    ("Integer","integer"), # 63
    ("ClassDeclarations", ""), # 64
]

# map_terminals = {
#     "^": "==",
#     "&": "&&",
#     "%": "+=",
#     "a": "false",
#     "b": "boolean",
#     "c": "class",
#     "d": "identifier",
#     "e": "EOF",
#     "f": "if",
#     "i": "int",
#     "l": "else",
#     "m": "main",
#     "n": "integer",
#     "o": "for",
#     "p": "public",
#     "r": "return",
#     "s": "static",
#     "t": "true",
#     "v": "void",
#     "w": "while",
#     "x": "extends",
#     "y": "System.out.println",
# }

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

terminals = list(map_terminals.keys())