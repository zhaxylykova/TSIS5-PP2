import re
line = str(input())
result = re.sub(r"[ ,.]", ":", line,2)
print(result)