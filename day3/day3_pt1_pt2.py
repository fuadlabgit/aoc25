
with open("input.txt", "r") as file:
    input = file.read() 

# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

# pt1
def process_line(l):
    buf = {i: [] for i in range(10)}
    for i, li in enumerate(l):
        buf[int(li)].append(i)

    for k in range(10):
        for m in range(10): 
            d1 = 9-k
            d2 = 9-m 
            b1 = buf[d1] 
            b2 = buf[d2]
            if len(b1) == 0 or len(b2) == 0: continue 
            if min(b1) < max(b2): return 10*d1 + d2
s = 0
for l in input.split("\n"):
    s+= process_line(l)
print(s)

# pt2 
n_max = 12 
def process_line(l):        
    digits = [int(d) for d in l]
    n = len(digits)
    to_remove = n - n_max
    stack = []
    for d in digits:
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)
    if to_remove > 0:
        stack = stack[:-to_remove]
    stack = stack[:n_max]
    best_jolt = 0
    for d in stack:
        best_jolt = best_jolt * 10 + d
    return best_jolt

s = 0
for l in input.split("\n"):
    s+= process_line(l)
print(s)
