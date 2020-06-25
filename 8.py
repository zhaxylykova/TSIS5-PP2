import re
line = str(input())
ans = '[A-Z]+[a-z]+$'
if re.search(ans, line):
    print("Found a match!")
else:
    print("No match!")    