import re
line = str(input())
if re.findall("z", line):
    print("yes")
else:
    print("no")
        