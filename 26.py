import re
number = int(input())
array = list()
for i in range(number):
    t = str(input())
    array.append(t)
for a in array:
    key = re.match(r"(P\w+)\W(P\w+)", a)
    if key:
        print(key.groups())
