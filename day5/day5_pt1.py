# read input
with open("input.txt", "r") as file:
    input = file.read() 
split1, split2 = input.split("\n\n")
ranges = []
for r in split1.split("\n"):
    a, b = r.split("-")
    ranges.append((int(a), int(b)))
avail = [int(r.strip()) for r in split2.split("\n")]

# pt.1
fresh = 0
for a in avail: 
    for r in ranges:
        if r[0] <= a <= r[1]:    
            fresh += 1 
            break 
print(fresh)
