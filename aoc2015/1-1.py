vals = []

s=input()
floor = 0
for c in s:
    if c == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
