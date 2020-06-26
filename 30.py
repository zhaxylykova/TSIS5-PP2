import re
line = str(input())
result = re.sub(r"Road", "Rd", line)
print(result)
