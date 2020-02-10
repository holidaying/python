import re
r=re.search(r'[1-9]\d2',"122sdfsdf")
print(r.group(0))
print(r.pos)
print(r.endPos)