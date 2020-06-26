import re
line = str(input())
key = r"\w+\S+[.]$"
if re.search(key, line):
    print("found a match!")
else:
    print("no match!")    