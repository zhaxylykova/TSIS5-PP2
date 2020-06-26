import re
line = str(input())
answer = re.sub(r" +", " ", line)
print(answer)