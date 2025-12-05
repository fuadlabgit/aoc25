# read input
with open("input.txt", "r") as file:
    input = file.read() 
split1, split2 = input.split("\n\n")
ranges = []
for r in split1.split("\n"):
    a, b = r.split("-")
    ranges.append((int(a), int(b)))
avail = [int(r.strip()) for r in split2.split("\n")]

# pt. 2
def merge_intervals(x, y):
    a, b = x 
    u, v = y 

    # a +----- + b   . . . . u +------+ v   
    if b < u: return [(a, b), (u, v)]

    # u +----- + v   . . . . a +------+ b
    if v < a: return [(u, v), (a, b)]

    """"
        a +----------------+ b 
    u +----------+ v 
    """
    return [(min(a, u), max(b, v))]

ranges = sorted(ranges, key=lambda x: x[0])
merged = [ranges[0]]
for interval in ranges[1:]:
    res = merge_intervals(merged[-1], interval)
    if len(res) == 1:
        merged[-1] = res[0]
    else:
        merged.append(interval)
c = 0
for s in merged:
    c+= s[1]-s[0] + 1
print(c)