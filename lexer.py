import re

class Token:
    def __init__(self, type: str, value: str, line_number: int, column_number: int) -> None:
        self.type = type
        self.value = value
        self.line_number = line_number
        self.column_number = column_number


STRING_DATA_TYPE = "STRING_DATA_TYPE"
INTEGER_DATA_TYPE = "INTEGER_DATA_TYPE"
BOOLEAN_DATA_TYPE = "BOOLEAN_DATA_TYPE"
DATA_TYPES = [
    STRING_DATA_TYPE,
    INTEGER_DATA_TYPE,
    BOOLEAN_DATA_TYPE,
]

PRINT = "PRINT"
WHILE = "WHILE"
IF = "IF"

PLUS = "PLUS"
MINUS = "MINUS"
DIVIDE = "DIVIDE"
MULTIPLY = "MULTIPLY"
ARITHMETIC_OPERATORS = [
    PLUS,
    MINUS,
    DIVIDE,
    MULTIPLY
]

ASSIGN = "ASSIGN"

EQUAL_TO = "EQUAL_TO"
NOT_EQUAL_TO = "NOT_EQUAL_TO"
MORE_THAN = "MORE_THAN"
MORE_THAN_OR_EQUAL_TO = "MORE_THAN_OR_EQUAL_TO"
LESS_THAN = "LESS_THAN"
LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
COMPARISON_OPERATORS = [
    EQUAL_TO,
    NOT_EQUAL_TO,
    MORE_THAN,
    MORE_THAN_OR_EQUAL_TO,
    LESS_THAN,
    LESS_THAN_OR_EQUAL_TO,
]

OPEN_BRACKET = "OPEN_BRACKET"
CLOSE_BRACKET = "CLOSE_BRACKET"
OPEN_CURLY_BRACKET = "OPEN_CURLY_BRACKET"
CLOSE_CURLY_BRACKET = "CLOSE_CURLY_BRACKET"
SEMICOLON = "SEMICOLON"
STRING_LITERAL = "STRING_LITERAL"
INTEGER_LITERAL = "NUMBER_LITERAL"
BOOLEAN_LITERAL = "BOOL_LITERAL"
IDENTIFIER = "IDENTIFIER"
# This token type acts as a placeholder
MISSING = "MISSING"


def get_tokens(source_code: str) -> list[Token]:
    tokens = []

    reserved_keywords = [
        ("bool", BOOLEAN_DATA_TYPE),
        ("int", INTEGER_DATA_TYPE),
        ("string", STRING_DATA_TYPE),
        ("print", PRINT),
        ("if", IF),
        ("while", WHILE),
        ("true", BOOLEAN_LITERAL),
        ("false", BOOLEAN_LITERAL),
    ]
    reserved_keywords_dictionary = dict(reserved_keywords)

    symbols: list[tuple[str, str]] = [
        (">=", MORE_THAN_OR_EQUAL_TO),
        ("<=", LESS_THAN_OR_EQUAL_TO),
        ("==", EQUAL_TO),
        ("!=", NOT_EQUAL_TO),
        ("+", PLUS),
        ("-", MINUS),
        ("/", DIVIDE),
        ("*", MULTIPLY),
        (">", MORE_THAN),
        ("<", LESS_THAN),
        ("=", ASSIGN),
        ("(", OPEN_BRACKET),
        (")", CLOSE_BRACKET),
        ("{", OPEN_CURLY_BRACKET),
        ("}", CLOSE_CURLY_BRACKET),
        (";", SEMICOLON),
    ]
    symbols_dictionary = dict(symbols)

    nonfixed_keywords = [
        (r"\".+\"", STRING_LITERAL),
        (r"\d+", INTEGER_LITERAL),
        (r"[a-zA-Z]\w*", IDENTIFIER),
    ]

    re_pattern = r"\w+|\".+\"|\s+"
    for symbol, type in symbols:
        for special_char in ["(", ")", "|", "+", "*"]:
            symbol = symbol.replace(special_char, f"\\{special_char}")

        re_pattern += r"|" + symbol

    for line_number, line in enumerate(source_code.split("\n")):
        line_number += 1
        for match in re.finditer(re_pattern, line):
            token = match.group()

            # Check if token is empty space
            if token == " " * len(token):
                continue

            column_number = match.span()[0] + 1

            # Check if token is a reserved keyword
            token_type = reserved_keywords_dictionary.get(token)

            # Check if token is a symbol
            if token_type == None:
                token_type = symbols_dictionary.get(token)

            # Check if token is a non-fixed token (i.e, string literal, number literal or variable name)
            if token_type == None:
                for pattern, type in nonfixed_keywords:
                    if __exact_match(pattern, token):
                        token_type = type
                        break

            if token_type == None:
                raise Exception(
                    f"Invalid Token {token} at line {line_number} and column {column_number}")

            tokens.append(Token(token_type, token, line_number, column_number))

    return tokens


def __exact_match(pattern, string) -> bool:
    match = re.match(pattern, string)
    return match != None and len(match.group()) == len(string)
