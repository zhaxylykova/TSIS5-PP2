import re
line = str(input())
res = re.sub(r'0','',line)
print(res)