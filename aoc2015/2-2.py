vals = []

while True:
        try:
            s=input()
            if s.strip() == '':
                continue
            vals.append(s)
        except EOFError:
            break

area_fn = lambda l,w,h: 2*l*w + 2*w*h + 2*h*l

ribbon = 0
for val in vals:
    [l,w,h] = map(int, val.split("x"))
    perimeter = 2 * min(l+w, w+h, h+l)
    ribbon += perimeter + (l*w*h)
print(ribbon)
