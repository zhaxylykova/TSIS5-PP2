import re
line = str(input())
if re.findall(r"\Bz\B", line):
    print("yes")
else:
    print("no")    