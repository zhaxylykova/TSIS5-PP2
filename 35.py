import re
line = str(input())
result = re.findall(r"\b\w{4,}\b", line)
print(result)