import re
line = str(input())
for i in re.finditer(r"\d+", line):
    print(i.group(0))
    print("Position:", i.start())