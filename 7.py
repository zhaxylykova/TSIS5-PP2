import re
line = str(input())
key = '^[a-z]+_[a-z]+$'
if re.search(key, line):
    print("Found a match!")
else:
    print("Not matched!")    