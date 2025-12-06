with open("input.txt", "r") as file:
    input = file.read() 
task = []
lines = input.split("\n")
for l in lines[:-1]:
    task.append(list(map(int, l.split())))
task = [list(row) for row in zip(*task)]
ops = lines[-1].split()

def apply(x, op):
    s = x[0]
    for i in range(1, len(x)):
        s = op(s, x[i])
    return s 
funcs = {"*": lambda x,y : x*y, "+": lambda x,y : x+y}
s = 0
for i, o in enumerate(ops):
    s += apply(task[i], funcs[o])
print(s)
