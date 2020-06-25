import re
line = str(input())
space = re.search(r"\s", line)
if space.start() == 0:
    print("No match!")
else:
    print("Found a match!")
