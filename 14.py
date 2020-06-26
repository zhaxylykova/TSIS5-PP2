import re
line = str(input())
key = "^[a-zA-Z0-9_]*$"
if re.search(key, line):
    print("found a match!")
else:
    print("no match!")    