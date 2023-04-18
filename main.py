from lexer import get_tokens
from tree_parser import get_parse_tree
from symbol_table import generate_symbol_table
from formatters import format_symbol_table, format_parse_tree

source_code = ""

with open("source_code.txt") as src:
    source_code = src.read()

tokens = get_tokens(source_code)

symbol_table = generate_symbol_table(tokens)

statements = get_parse_tree(tokens)

with open("output\symbol_table_output.txt", "w", encoding="utf-16") as dist:
    dist.write(format_symbol_table(symbol_table) + "\n")

with open("output\parse_tree_output.txt", "w", encoding="utf-16") as dist:
    dist.write(format_parse_tree(statements))
