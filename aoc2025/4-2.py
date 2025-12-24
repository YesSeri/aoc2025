vals = []

while True:
        try:
            s=input()
            if s.strip() == '':
                continue
            vals.append(list(s))
        except EOFError:
            break



def is_at(x, y, vals):
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= len(vals):
        return False
    if y >= len(vals[x]):
        return False
    return vals[x][y] == '@'
    

dirs = [
(-1,1), (-1,0), (-1,-1),
(0,-1),  (0,1), 
(1,-1),  (1,0), (1,1),
]

v = vals[0]
x=0
prev_x = -1
while x != prev_x:
    prev_x = x
    for i in range(len(vals)):
        for j in range(len(vals[i])):
            k = 0
            if vals[i][j] != '@':
                continue
            for dx,dy in dirs:
                if is_at(i+dx, j+dy, vals):
                    k+=1

            if k < 4:
                vals[i][j] = '.'
                x+=1

print('x', x)
        



