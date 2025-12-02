print('hello')
vals = []

while True:
        try:
            s=input()
            if s.strip() == '':
                continue
            vals.append(s)
        except EOFError:
            break

start = 50
zero = 0
for val in vals:
    dir = val[0]
    num = int(val[1:])
    while num != 0:
        if dir == 'R':
            start += 1
        else:
            start -= 1
        num -= 1
        if start%100 == 0:
            zero += 1
print(zero)
