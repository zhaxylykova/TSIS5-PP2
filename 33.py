import re
line = str(input())
res = re.findall(r"\b\w{5}\b", line)
print(res)
