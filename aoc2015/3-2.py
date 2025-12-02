s=input()

h = set([])

loc_s=[0,0]
loc_r=[0,0]
for i, c in enumerate(s):
    if i % 2 == 0:
        loc = loc_s
    else:
        loc = loc_r
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
