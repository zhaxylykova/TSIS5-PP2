import re
line = str(input())
key = "a.*?b$"
if re.search(key, line):
    print("Found a match!")
else:
    print("No match!")    