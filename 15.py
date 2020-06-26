import re
line = str(input())

key = re.compile(r"^5")
if key.match(line):
    print("ok")
else:
    print("no")    