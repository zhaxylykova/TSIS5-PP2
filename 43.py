import re
line = str(input())
result = re.findall("[A-Z][^A-Z]*", line)
print(result)