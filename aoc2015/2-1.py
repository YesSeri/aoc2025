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

total_area = 0
for val in vals:
    [l,w,h] = map(int, val.split("x"))
    smallest_side = min(l*w, w*h, h*l)
    total_area += area_fn(l,w,h) + smallest_side
print(total_area)
