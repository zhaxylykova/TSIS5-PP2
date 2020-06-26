import re
line = str(input())
answer = re.split(r"\D+", line)
for p in answer:
    print(p)