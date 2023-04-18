import re

identifier = input("Identifier: ")

match = re.match("[a-zA-Z]\w+", identifier)

if match != None and match.group() == identifier:
    print("Valid!")
else:
    print("Invalid!")
