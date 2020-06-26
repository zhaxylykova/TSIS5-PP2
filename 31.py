import re
line = str(input())
result = re.sub(r"[ ,.]", ":", line)
print(result)
