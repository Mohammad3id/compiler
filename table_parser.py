_parse_table = {}

with open("parse_table.txt", encoding="utf-16") as f:
    table_str = f.read()

    if table_str[-1] == "\n":
        table_str = table_str[:-1]

    rows = table_str.split("\n")
    rows = [row for i, row in enumerate(rows) if i % 2 == 1]

    table = []

    for row in rows:
        row_items = [item.strip() for item in row.split("||")]
        table.append(row_items)

    terminal_terms = table[0][1:]

    for row in table[1:]:
        non_terminal_term = row[0]
        _parse_table[non_terminal_term] = {}
        for i, rule in enumerate(row[1:]):
            if rule == "":
                rule = "None"
            terminal_term = terminal_terms[i]
            _parse_table[non_terminal_term][terminal_term] = rule


def get_rule(non_terminal_term: str, terminal_term: str):
    if not non_terminal_term in _parse_table.keys():
        return f"None-Terminal term ({non_terminal_term}) doesn't exist in grammar"

    if not terminal_term in _parse_table[non_terminal_term].keys():
        return f"Terminal term ({terminal_term}) doesn't exist in grammar"

    return _parse_table[non_terminal_term][terminal_term]


if __name__ == "__main__":
    while True:
        non_terminal_term = input("Non-Terminal term: ")
        terminal_term = input("Terminal term: ")
        print(get_rule(non_terminal_term, terminal_term))
        print("------------------------------")
