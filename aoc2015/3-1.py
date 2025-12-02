s=input()

h = set([])

loc=[0,0]
for c in s:
    if c == '>':
        loc[0] += 1
    if c == '<':
        loc[0] -= 1
    if c == 'v':
        loc[1] += 1
    if c == '^':
        loc[1] -= 1
    h.add((loc[0], loc[1]))
print(len(h))
