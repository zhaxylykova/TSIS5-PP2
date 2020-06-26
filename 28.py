import re
line = str(input())
result = re.findall(r"[ae]\w+", line)
print(result)
