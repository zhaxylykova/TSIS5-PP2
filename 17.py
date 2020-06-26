import re
line = str(input())
key = ".[0-9]$"
if re.search(key, line):
    print("ok")
else:
    print("no match!")    