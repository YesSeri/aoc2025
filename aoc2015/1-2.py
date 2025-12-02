
vals = []

s=input()
floor = 0
idx = 0
for c in s:
    idx+=1
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        break

print(idx)
