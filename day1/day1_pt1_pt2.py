
with open("input.txt", "r") as file:
    input = file.read() 

# input = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

# input = """R51
# R100"""

# pt1 
p = 50
s = 0

for l in input.split("\n"): 
    x = int(l[1:])
    dp = -x if l[0]=="L" else x
    p+= dp 
    p = p%100
    if p == 0:
        s += 1 
print(s)

# pt2
p = 50
s = 0
for l in input.split("\n"): 
    x = int(l[1:])
    dp = -x if l[0]=="L" else x
    for j in range(abs(dp)):
        if dp > 0: 
            p += 1 
        elif dp < 0:
            p -= 1 
        if p == 100:
            p = 0
        if p < 0: 
            p = 99
        # p %= 100
        if p == 0:
            s += 1
print(s)


# pt2 (alternative)
p = 50
s = 0
for l in input.split("\n"):
    if not l:
        continue
    x = int(l[1:])
    u = -1 if l[0] == "L" else 1
    steps = abs(x)
    full_loops = steps // 100
    s += full_loops
    rem = steps % 100
    if u > 0: 
        dist = (100 - p) % 100
    else:
        dist = p % 100
    if 0 < dist <= rem:
        s += 1         
    p = (p + u * rem) % 100
print(s, "(alternative)")