import re
line = str(input())
for i in re.finditer(r"\w+ly", line):
    print(i.group(0))
    print("Positions:", i.start(), "-", i.end())