vals = []

while True:
        try:
            s=input()
            vals.append(s)
        except EOFError:
            break

vowel_set = set(['a','e', 'i', 'o', 'u']) 
verboten = set(['ab', 'cd', 'pq', 'xy'])
i = 0
for val in vals:
    j = 0
    for c in val:
        if c in vowel_set:
            j += 1
    if j < 3:
        continue
    is_rep = False
    for k,c in enumerate(val[0:-1]):
        if val[k] == val[k+1]:
            is_rep = True
    if not is_rep:
        continue
    is_verboten = False

    is_verboten = False
    for v in verboten:
        if v in val:
            is_verboten = True
            break

    if is_verboten:
        continue

    i += 1

print(i)
