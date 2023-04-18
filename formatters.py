def format_symbol_table(symbol_table: dict):
    table_ds = [
        ["Identifier", "Data Type", "Address", "Reference Lines", "Dimensions"],
    ]

    for key in symbol_table.keys():
        identifier = key
        data_type = symbol_table[key]["data_type"]
        address = hex(symbol_table[key]["address"])
        reference_lines = ", ".join(
            [str(n) for n in symbol_table[key]["reference_lines"]])
        if len(reference_lines) == 0:
            reference_lines = "None"
        dimensions = str(symbol_table[key]["dimensions"])

        table_ds.append([identifier, data_type, address,
                        reference_lines, dimensions])

    column_widths = [
        max(len(row[i]) for row in table_ds) + 2 for i in range(5)
    ]

    formatted_symbol_table = "―" * (sum(column_widths) + 8) + "\n"

    for row in table_ds:
        formatted_symbol_table += "||".join([cell.center(width)
                                             for cell, width in zip(row, column_widths)])
        formatted_symbol_table += "\n" + "―" * (sum(column_widths) + 8) + "\n"

    return formatted_symbol_table


def format_parse_tree(statements):
    formatted_parse_tree = ""
    for statement in statements:
        formatted_parse_tree += str(statement)

    return formatted_parse_tree


def add_indentation(string: str, count=1) -> str:
    return ("    " * count + string.replace("\n", "\n" + "    " * count))[:-count * 4]
