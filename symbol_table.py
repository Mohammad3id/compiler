from lexer import Token, DATA_TYPES, IDENTIFIER, BOOLEAN_DATA_TYPE, INTEGER_DATA_TYPE, STRING_DATA_TYPE


def generate_symbol_table(tokens: list[Token]):
    symbol_table = {}
    token_index = 0
    next_address = 0
    while token_index < len(tokens):
        token = tokens[token_index]
        if token.type in DATA_TYPES:
            token_index += 1
            if token_index == len(tokens) or tokens[token_index].type != IDENTIFIER:
                raise Exception(
                    f"Expected a variable name after {token.value} at line {token.line_number}")

            data_type = token.value

            variable_token = tokens[token_index]

            if symbol_table.get(variable_token.value) != None:
                raise Exception(
                    f"Error at line {token.line_number}: variable {variable_token.value} is already declared.")

            symbol_table[variable_token.value] = {
                "data_type": data_type,
                "address": next_address,
                "line_of_declaration": token.line_number,
                "reference_lines": set(),
                "dimensions": 0,
            }

            if token.type == BOOLEAN_DATA_TYPE:
                next_address += 1
            elif token.type == INTEGER_DATA_TYPE:
                next_address += 4
            elif token.type == STRING_DATA_TYPE:
                next_address += len(token.value)

        elif token.type == IDENTIFIER:
            if symbol_table.get(token.value) == None:
                raise Exception(
                    f"Error at line {token.line_number}: variable {token.value} is not declared.")

            symbol_table[token.value]["reference_lines"].add(token.line_number)

        token_index += 1

    return symbol_table
