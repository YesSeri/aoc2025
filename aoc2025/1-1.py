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
    if dir == 'R':
        start += num
    else:
        start -= num
    if start%100 == 0:
        zero += 1
print(zero)
