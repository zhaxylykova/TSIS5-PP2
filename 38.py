import re
line = str(input())
output = re.findall(r'"(.*?)"', line)
print(output)