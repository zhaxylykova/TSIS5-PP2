import re
line = str(input())
answer = re.sub(r"\s+", "", line)
print(answer)