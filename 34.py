import re
line = str(input())
result = re.findall(r"\b\w{3,5}\b", line)
print(result)