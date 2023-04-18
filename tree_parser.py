import lexer as Lex
from formatters import add_indentation


class Statement:
    def __str__(self) -> str:
        return ""

    def get_tokens(self) -> list[Lex.Token]:
        return []


class WhileStatement(Statement):
    def __init__(
        self,
        while_token: Lex.Token,
        open_braket_token: Lex.Token,
        boolean_expression_tokens: list[Lex.Token],
        close_braket_token: Lex.Token,
        open_curly_braket_token: Lex.Token,
        statements: list[Statement],
        close_curly_braket_token: Lex.Token,
    ) -> None:
        self.while_token = while_token
        self.open_braket_token = open_braket_token
        self.boolean_expression_tokens = boolean_expression_tokens
        self.close_braket_token = close_braket_token
        self.open_curly_braket_token = open_curly_braket_token
        self.statements = statements
        self.close_curly_braket_token = close_curly_braket_token

    def get_tokens(self) -> list[Lex.Token]:
        statements_tokens = []
        for statement in self.statements:
            for token in statement.get_tokens():
                statements_tokens.append(token)
        return [
            self.while_token,
            self.open_braket_token,
            *self.boolean_expression_tokens,
            self.close_braket_token,
            self.open_curly_braket_token,
            *statements_tokens,
            self.close_curly_braket_token,
        ]

    def __str__(self) -> str:
        result = ""
        result += f"WHILE_STATEMENT: line {self.while_token.line_number}\n"
        result += f"    {self.while_token.type}: {self.while_token.value}\n"
        result += f"    {self.open_braket_token.type}: {self.open_braket_token.value}\n"
        result += f"    BOOLEAN_EXPRESSION:\n"
        for token in self.boolean_expression_tokens:
            result += f"         {token.type}: {token.value}\n"
        result += f"    {self.close_braket_token.type}: {self.close_braket_token.value}\n"
        result += f"    {self.open_curly_braket_token.type}: {self.open_curly_braket_token.value}\n"
        result += f"    STATEMENTS:\n"
        statements_string = ""
        for statement in self.statements:
            statements_string += str(statement)
        result += add_indentation(str(statements_string), count=2)
        result += f"    {self.close_curly_braket_token.type}: {self.close_curly_braket_token.value}\n"

        return result


class IfStatement(Statement):
    def __init__(
        self,
        if_token: Lex.Token,
        open_braket_token: Lex.Token,
        boolean_expression_tokens: list[Lex.Token],
        close_braket_token: Lex.Token,
        open_curly_braket_token: Lex.Token,
        statements: list[Statement],
        close_curly_braket_token: Lex.Token,
    ) -> None:
        self.if_token = if_token
        self.open_braket_token = open_braket_token
        self.boolean_expression_tokens = boolean_expression_tokens
        self.close_braket_token = close_braket_token
        self.open_curly_braket_token = open_curly_braket_token
        self.statements = statements
        self.close_curly_braket_token = close_curly_braket_token

    def get_tokens(self) -> list[Lex.Token]:
        statements_tokens = []
        for statement in self.statements:
            for token in statement.get_tokens():
                statements_tokens.append(token)
        return [
            self.if_token,
            self.open_braket_token,
            *self.boolean_expression_tokens,
            self.close_braket_token,
            self.open_curly_braket_token,
            *statements_tokens,
            self.close_curly_braket_token,
        ]

    def __str__(self) -> str:
        result = ""
        result += f"IF_STATEMENT: line {self.if_token.line_number}\n"
        result += f"    {self.if_token.type}: {self.if_token.value}\n"
        result += f"    {self.open_braket_token.type}: {self.open_braket_token.value}\n"
        result += f"    BOOLEAN_EXPRESSION:\n"
        for token in self.boolean_expression_tokens:
            result += f"         {token.type}: {token.value}\n"
        result += f"    {self.close_braket_token.type}: {self.close_braket_token.value}\n"
        result += f"    {self.open_curly_braket_token.type}: {self.open_curly_braket_token.value}\n"
        result += f"    STATEMENTS:\n"
        statements_string = ""
        for statement in self.statements:
            statements_string += str(statement)
        result += add_indentation(str(statements_string), count=2)
        result += f"    {self.close_curly_braket_token.type}: {self.close_curly_braket_token.value}\n"

        return result


class PrintStatement(Statement):
    def __init__(
        self,
        print_token: Lex.Token,
        open_braket_token: Lex.Token,
        expression_tokens: list[Lex.Token],
        close_braket_token: Lex.Token,
        semicolon_token: Lex.Token,
    ) -> None:
        self.print_token = print_token
        self.open_braket_token = open_braket_token
        self.expression_tokens = expression_tokens
        self.close_braket_token = close_braket_token
        self.semicolon_token = semicolon_token

    def get_tokens(self) -> list[Lex.Token]:
        return [
            self.print_token,
            self.open_braket_token,
            *self.expression_tokens,
            self.close_braket_token,
            self.semicolon_token,
        ]

    def __str__(self) -> str:
        result = ""
        result += f"PRINT_STATEMENT: line {self.print_token.line_number}\n"
        result += f"    {self.print_token.type}: {self.print_token.value}\n"
        result += f"    {self.open_braket_token.type}: {self.open_braket_token.value}\n"
        result += f"    EXPRESSION:\n"
        for token in self.expression_tokens:
            result += f"         {token.type}: {token.value}\n"
        result += f"    {self.close_braket_token.type}: {self.close_braket_token.value}\n"
        result += f"    {self.semicolon_token.type}: {self.semicolon_token.value}\n"

        return result


class AssignmentStatement(Statement):
    def __init__(
        self,
        identifier_token: Lex.Token,
        assignment_operator_token: Lex.Token,
        expression_tokens: list[Lex.Token],
        semicolon_token: Lex.Token,
    ) -> None:
        self.identifier_token = identifier_token
        self.assignment_operatorToken = assignment_operator_token
        self.expression_tokens = expression_tokens
        self.semicolon_token = semicolon_token

    def get_tokens(self) -> list[Lex.Token]:
        return [
            self.identifier_token,
            self.assignment_operatorToken,
            *self.expression_tokens,
            self.semicolon_token,
        ]

    def __str__(self) -> str:
        result = ""
        result += f"ASSIGNMENT_STATEMENT: line {self.identifier_token.line_number}\n"
        result += f"    {self.identifier_token.type}: {self.identifier_token.value}\n"
        result += f"    {self.assignment_operatorToken.type}: {self.assignment_operatorToken.value}\n"
        result += f"    EXPRESSION:\n"
        for token in self.expression_tokens:
            result += f"         {token.type}: {token.value}\n"
        result += f"    {self.semicolon_token.type}: {self.semicolon_token.value}\n"

        return result


class DeclarationStatement(Statement):
    def __init__(
        self,
        data_type_token: Lex.Token,
        identifier_token: Lex.Token,
        assignment_operator_token: Lex.Token,
        expression_tokens: list[Lex.Token],
        semicolon_token: Lex.Token,
    ) -> None:
        self.data_type_token = data_type_token
        self.identifier_token = identifier_token
        self.assignment_operatorToken = assignment_operator_token
        self.expression_tokens = expression_tokens
        self.semicolon_token = semicolon_token

    def get_tokens(self) -> list[Lex.Token]:
        return [
            self.data_type_token,
            self.identifier_token,
            self.assignment_operatorToken,
            *self.expression_tokens,
            self.semicolon_token,
        ]

    def __str__(self) -> str:
        result = ""
        result += f"DECLARATION_STATEMENT: line {self.data_type_token.line_number}\n"
        result += f"    {self.data_type_token.type}: {self.data_type_token.value}\n"
        result += f"    {self.identifier_token.type}: {self.identifier_token.value}\n"
        result += f"    {self.assignment_operatorToken.type}: {self.assignment_operatorToken.value}\n"
        result += f"    EXPRESSION:\n"
        for token in self.expression_tokens:
            result += f"         {token.type}: {token.value}\n"
        result += f"    {self.semicolon_token.type}: {self.semicolon_token.value}\n"

        return result


def get_parse_tree(tokens: list[Lex.Token]) -> list[Statement]:
    return _parse_statements(tokens)


def _parse_statements(tokens: list[Lex.Token]) -> list[Statement]:
    tree = []

    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token.type in Lex.DATA_TYPES:
            declaration_statement = _parse_declaration_statement(tokens[i:])
            tree.append(declaration_statement)
            i += len(declaration_statement.get_tokens())

        elif token.type == Lex.IDENTIFIER:
            assignment_statement = _parse_assignment_statement(tokens[i:])
            tree.append(assignment_statement)
            i += len(assignment_statement.get_tokens())

        elif token.type == Lex.PRINT:
            print_statement = _parse_print_statement(tokens[i:])
            tree.append(print_statement)
            i += len(print_statement.get_tokens())

        elif token.type == Lex.IF:
            if_statement = _parse_if_statement(tokens[i:])
            tree.append(if_statement)
            i += len(if_statement.get_tokens())

        elif token.type == Lex.WHILE:
            while_statement = _parse_while_statement(tokens[i:])
            tree.append(while_statement)
            i += len(while_statement.get_tokens())

        else:
            i += 1

    return tree


def _parse_while_statement(tokens: list[Lex.Token]):
    if len(tokens) < 7:
        for i in range(7 - len(tokens)):
            tokens.append(Lex.Token(type=Lex.MISSING, value="",
                          column_number=0, line_number=0))

    while_token = tokens[0]
    open_braket_token = tokens[1]

    if while_token.type != Lex.WHILE:
        raise Exception(
            f"Parser Error: Expected a \"while\" at line {while_token.line_number} and column {while_token.column_number}")
    if open_braket_token.type != Lex.OPEN_BRACKET:
        raise Exception(
            f"Parser Error: Expected an open braket at line {while_token.line_number} and column {while_token.column_number + len(while_token.value)}")

    expression_first_token = tokens[2]

    if expression_first_token.type == Lex.BOOLEAN_LITERAL and tokens[3].type == Lex.CLOSE_BRACKET:
        expression_tokens = [expression_first_token]
    elif expression_first_token.type in [Lex.INTEGER_LITERAL, Lex.IDENTIFIER]:
        operator_token = tokens[3]
        if operator_token.type in Lex.COMPARISON_OPERATORS:
            expression_tokens = _parse_boolean_expression(
                tokens[2:])
        else:
            raise Exception(
                f"Parser Error: Expected a comparison operator at line {expression_first_token.line_number} and column {expression_first_token.column_number + len(expression_first_token.value)}")
    else:
        raise Exception(
            f"Parser Error: Expected a boolean expression at line {expression_first_token.line_number} and column {expression_first_token.column_number}")

    close_braket_token = tokens[2 + len(expression_tokens)]

    if close_braket_token.type != Lex.CLOSE_BRACKET:
        raise Exception(
            f"Parser Error: Expected a closing braket at line {expression_tokens[-1].line_number} and column {expression_tokens[-1].column_number + len(expression_tokens[-1].value)}")

    open_curly_braket_token = tokens[3 + len(expression_tokens)]

    if open_curly_braket_token.type != Lex.OPEN_CURLY_BRACKET:
        raise Exception(
            f"Parser Error: Expected an open curly braket at line {expression_tokens[-1].line_number} and column {expression_tokens[-1].column_number + len(expression_tokens[-1].value)}")

    statements_tokens = []

    close_curly_braket_token = None

    unclosed_curly_brakets_count = 1

    for token in tokens[4 + len(expression_tokens):]:
        if token.type == Lex.OPEN_CURLY_BRACKET:
            unclosed_curly_brakets_count += 1

        if token.type == Lex.CLOSE_CURLY_BRACKET:
            unclosed_curly_brakets_count -= 1

        if unclosed_curly_brakets_count == 0:
            close_curly_braket_token = token
            break

        statements_tokens.append(token)

    if close_curly_braket_token == None:
        if len(statements_tokens) == 0:
            lastToken = open_curly_braket_token
        else:
            lastToken = statements_tokens[-1]

        raise Exception(
            f"Parser Error: Expected a closing curly braket at line {lastToken.line_number} and column {lastToken.column_number + len(lastToken.value)}")

    statements = _parse_statements(statements_tokens)

    return WhileStatement(
        while_token,
        open_braket_token,
        expression_tokens,
        close_braket_token,
        open_curly_braket_token,
        statements,
        close_curly_braket_token,
    )


def _parse_if_statement(tokens: list[Lex.Token]):
    if len(tokens) < 7:
        for i in range(7 - len(tokens)):
            tokens.append(Lex.Token(type=Lex.MISSING, value="",
                          column_number=0, line_number=0))

    if_token = tokens[0]
    open_braket_token = tokens[1]

    if if_token.type != Lex.IF:
        raise Exception(
            f"Parser Error: Expected an \"if\" at line {if_token.line_number} and column {if_token.column_number}")
    if open_braket_token.type != Lex.OPEN_BRACKET:
        raise Exception(
            f"Parser Error: Expected an open braket at line {if_token.line_number} and column {if_token.column_number + len(if_token.value)}")

    expression_first_token = tokens[2]

    if expression_first_token.type == Lex.BOOLEAN_LITERAL and tokens[3].type == Lex.CLOSE_BRACKET:
        expression_tokens = [expression_first_token]
    elif expression_first_token.type in [Lex.INTEGER_LITERAL, Lex.IDENTIFIER]:
        operator_token = tokens[3]
        if operator_token.type in Lex.COMPARISON_OPERATORS:
            expression_tokens = _parse_boolean_expression(
                tokens[2:])
        else:
            raise Exception(
                f"Parser Error: Expected a comparison operator at line {expression_first_token.line_number} and column {expression_first_token.column_number + len(expression_first_token.value)}")
    else:
        raise Exception(
            f"Parser Error: Expected a boolean expression at line {expression_first_token.line_number} and column {expression_first_token.column_number}")

    close_braket_token = tokens[2 + len(expression_tokens)]

    if close_braket_token.type != Lex.CLOSE_BRACKET:
        raise Exception(
            f"Parser Error: Expected a closing braket at line {expression_tokens[-1].line_number} and column {expression_tokens[-1].column_number + len(expression_tokens[-1].value)}")

    open_curly_braket_token = tokens[3 + len(expression_tokens)]

    if open_curly_braket_token.type != Lex.OPEN_CURLY_BRACKET:
        raise Exception(
            f"Parser Error: Expected an open curly braket at line {expression_tokens[-1].line_number} and column {expression_tokens[-1].column_number + len(expression_tokens[-1].value)}")

    statements_tokens = []

    close_curly_braket_token = None

    unclosed_curly_brakets_count = 1

    for token in tokens[4 + len(expression_tokens):]:
        if token.type == Lex.OPEN_CURLY_BRACKET:
            unclosed_curly_brakets_count += 1

        if token.type == Lex.CLOSE_CURLY_BRACKET:
            unclosed_curly_brakets_count -= 1

        if unclosed_curly_brakets_count == 0:
            close_curly_braket_token = token
            break

        statements_tokens.append(token)

    if close_curly_braket_token == None:
        if len(statements_tokens) == 0:
            lastToken = open_curly_braket_token
        else:
            lastToken = statements_tokens[-1]

        raise Exception(
            f"Parser Error: Expected a closing curly braket at line {lastToken.line_number} and column {lastToken.column_number + len(lastToken.value)}")

    statements = _parse_statements(statements_tokens)

    return IfStatement(
        if_token,
        open_braket_token,
        expression_tokens,
        close_braket_token,
        open_curly_braket_token,
        statements,
        close_curly_braket_token,
    )


def _parse_print_statement(tokens: list[Lex.Token]):
    if len(tokens) < 5:
        for i in range(5 - len(tokens)):
            tokens.append(Lex.Token(type=Lex.MISSING, value="",
                          column_number=0, line_number=0))

    print_token = tokens[0]
    open_braket_token = tokens[1]

    if print_token.type != Lex.PRINT:
        raise Exception(
            f"Parser Error: Expected a \"print\" at line {print_token.line_number} and column {print_token.column_number}")
    if open_braket_token.type != Lex.OPEN_BRACKET:
        raise Exception(
            f"Parser Error: Expected an open braket at line {print_token.line_number} and column {print_token.column_number + len(print_token.value)}")

    expression_first_token = tokens[2]

    if expression_first_token.type == Lex.STRING_LITERAL:
        expression_tokens = [expression_first_token]
    elif expression_first_token.type in [Lex.INTEGER_LITERAL, Lex.BOOLEAN_LITERAL, Lex.IDENTIFIER] and tokens[3].type == Lex.CLOSE_BRACKET:
        expression_tokens = [expression_first_token]
    elif expression_first_token.type in [Lex.INTEGER_LITERAL, Lex.IDENTIFIER]:
        operator_token = tokens[3]
        if operator_token.type in Lex.ARITHMETIC_OPERATORS:
            expression_tokens = _parse_numerical_expression(
                tokens[2:])
        elif operator_token.type in Lex.COMPARISON_OPERATORS:
            expression_tokens = _parse_boolean_expression(
                tokens[2:])
        else:
            raise Exception(
                f"Parser Error: Expected an arithmetic operator, comparison operator, or a closing braket at line {expression_first_token.line_number} and column {expression_first_token.column_number + len(expression_first_token.value)}")
    else:
        raise Exception(
            f"Parser Error: Expected an expression at line {expression_first_token.line_number} and column {expression_first_token.column_number}")

    close_braket_token = tokens[2 + len(expression_tokens)]

    if close_braket_token.type != Lex.CLOSE_BRACKET:
        raise Exception(
            f"Parser Error: Expected a closing braket at line {expression_tokens[-1].line_number} and column {expression_tokens[-1].column_number + len(expression_tokens[-1].value)}")

    semicolon_token = tokens[3 + len(expression_tokens)]

    if semicolon_token.type != Lex.SEMICOLON:
        raise Exception(
            f"Parser Error: Expected a semicolon at line {expression_tokens[-1].line_number} and column {expression_tokens[-1].column_number + len(expression_tokens[-1].value)}")

    return PrintStatement(
        print_token,
        open_braket_token,
        expression_tokens,
        close_braket_token,
        semicolon_token,
    )


def _parse_assignment_statement(tokens: list[Lex.Token]):
    if len(tokens) < 4:
        for i in range(4 - len(tokens)):
            tokens.append(Lex.Token(type=Lex.MISSING, value="",
                          column_number=0, line_number=0))

    identifier_token = tokens[0]
    assignment_operator_token = tokens[1]

    if identifier_token.type != Lex.IDENTIFIER:
        raise Exception(
            f"Parser Error: Expected an identifier at line {identifier_token.line_number} and column {identifier_token.column_number}")
    if assignment_operator_token.type != Lex.ASSIGN:
        raise Exception(
            f"Parser Error: Expected an assignment operator at line {identifier_token.line_number} and column {identifier_token.column_number + len(identifier_token.value)}")

    assignment_value_expression_first_token = tokens[2]

    if assignment_value_expression_first_token.type == Lex.STRING_LITERAL:
        assignment_value_expression_tokens = [
            assignment_value_expression_first_token]
    elif assignment_value_expression_first_token.type in [Lex.INTEGER_LITERAL, Lex.BOOLEAN_LITERAL, Lex.IDENTIFIER] and tokens[3].type == Lex.SEMICOLON:
        assignment_value_expression_tokens = [
            assignment_value_expression_first_token]
    elif assignment_value_expression_first_token.type in [Lex.INTEGER_LITERAL, Lex.IDENTIFIER]:
        operator_token = tokens[3]
        if operator_token.type in Lex.ARITHMETIC_OPERATORS:
            assignment_value_expression_tokens = _parse_numerical_expression(
                tokens[2:])
        elif operator_token.type in Lex.COMPARISON_OPERATORS:
            assignment_value_expression_tokens = _parse_boolean_expression(
                tokens[2:])
        else:
            raise Exception(
                f"Parser Error: Expected an arithmetic operator, comparison operator, or a semicolon at line {assignment_value_expression_first_token.line_number} and column {assignment_value_expression_first_token.column_number + len(assignment_value_expression_first_token.value)}")
    else:
        raise Exception(
            f"Parser Error: Expected an expression at line {assignment_value_expression_first_token.line_number} and column {assignment_value_expression_first_token.column_number}")

    semicolon_token = tokens[2 + len(assignment_value_expression_tokens)]

    if semicolon_token.type != Lex.SEMICOLON:
        raise Exception(
            f"Parser Error: Expected a semiColon at line {assignment_value_expression_tokens[-1].line_number} and column {assignment_value_expression_tokens[-1].column_number + len(assignment_value_expression_tokens[-1].value)}")

    return AssignmentStatement(
        identifier_token=identifier_token,
        assignment_operator_token=assignment_operator_token,
        expression_tokens=assignment_value_expression_tokens,
        semicolon_token=semicolon_token
    )


def _parse_declaration_statement(tokens: list[Lex.Token]):
    if len(tokens) < 5:
        for i in range(5 - len(tokens)):
            tokens.append(Lex.Token(type=Lex.MISSING, value="",
                          column_number=0, line_number=0))

    data_type_token = tokens[0]
    identifier_token = tokens[1]
    assignment_operator_token = tokens[2]

    if data_type_token.type not in Lex.DATA_TYPES:
        raise Exception(
            f"Parser Error: Expected a data type at line {data_type_token.line_number} and column {data_type_token.column_number}")
    if identifier_token.type != Lex.IDENTIFIER:
        raise Exception(
            f"Parser Error: Expected an identifier at line {data_type_token.line_number} and column {data_type_token.column_number + len(data_type_token.value)}")
    if assignment_operator_token.type != Lex.ASSIGN:
        raise Exception(
            f"Parser Error: Expected an assignment operator at line {identifier_token.line_number} and column {identifier_token.column_number + len(identifier_token.value)}")

    if data_type_token.type == Lex.INTEGER_DATA_TYPE:
        assignment_value_expression_tokens = _parse_numerical_expression(
            tokens[3:])
    elif data_type_token.type == Lex.BOOLEAN_DATA_TYPE:
        assignment_value_expression_tokens = _parse_boolean_expression(
            tokens[3:])
    elif data_type_token.type == Lex.STRING_DATA_TYPE:
        assignment_value_expression_tokens = [tokens[3]]
        if assignment_value_expression_tokens[0].type != Lex.STRING_LITERAL:
            raise Exception(
                f"Parser Error: Expected a string value at line {assignment_operator_token.line_number} and column {assignment_operator_token.column_number + len(assignment_operator_token.value)}")

    semi_colon_token = tokens[3 + len(assignment_value_expression_tokens)]

    if semi_colon_token.type != Lex.SEMICOLON:
        raise Exception(
            f"Parser Error: Expected a semiColon at line {assignment_value_expression_tokens[-1].line_number} and column {assignment_value_expression_tokens[-1].column_number + len(assignment_value_expression_tokens[-1].value)}")

    return DeclarationStatement(
        data_type_token=data_type_token,
        identifier_token=identifier_token,
        assignment_operator_token=assignment_operator_token,
        expression_tokens=assignment_value_expression_tokens,
        semicolon_token=semi_colon_token
    )


def _parse_numerical_expression(tokens: list[Lex.Token]):
    expression_tokens = []

    first_token = tokens[0]
    if first_token.type not in [Lex.IDENTIFIER, Lex.INTEGER_LITERAL]:
        raise Exception(
            f"Parser Error: Expected a numerical expression at line {first_token.line_number} and column {first_token.column_number}")

    expression_tokens.append(first_token)

    i = 1

    while True:
        if len(tokens) == i or tokens[i].type not in Lex.ARITHMETIC_OPERATORS:
            return expression_tokens

        operator_token = tokens[i]

        if len(tokens) == i + 1 or tokens[i + 1].type not in [Lex.IDENTIFIER, Lex.INTEGER_LITERAL]:
            raise Exception(
                f"Parser Error: Expected a numerical expression at line {operator_token.line_number} and column {operator_token.column_number + len(operator_token.value)}")

        numerical_value_token = tokens[i + 1]

        expression_tokens.append(operator_token)
        expression_tokens.append(numerical_value_token)

        i += 2


def _parse_boolean_expression(tokens: list[Lex.Token]):
    expression_tokens = []

    first_token = tokens[0]

    if first_token.type not in [Lex.IDENTIFIER, Lex.INTEGER_LITERAL, Lex.BOOLEAN_LITERAL]:
        raise Exception(
            f"Parser Error: Expected a boolean expression at line {first_token.line_number} and column {first_token.column_number}")

    expression_tokens.append(first_token)

    if first_token.type == Lex.BOOLEAN_LITERAL:
        return expression_tokens

    if len(tokens) == 1 or tokens[1].type not in Lex.COMPARISON_OPERATORS:
        raise Exception(
            f"Parser Error: Expected a comparison operator at line {first_token.line_number} and column {first_token.column_number + len(first_token.value)}")

    operator_token = tokens[1]

    expression_tokens.append(operator_token)

    if len(tokens) == 2 or tokens[2].type not in [Lex.IDENTIFIER, Lex.INTEGER_LITERAL]:
        raise Exception(
            f"Parser Error: Expected a numerical value at line {operator_token.line_number} and column {operator_token.column_number + len(operator_token.value)}")

    last_token = tokens[2]

    expression_tokens.append(last_token)

    return expression_tokens
