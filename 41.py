import re
line = str(input())
answer = re.sub(r"\W+", "", line)
print(answer)