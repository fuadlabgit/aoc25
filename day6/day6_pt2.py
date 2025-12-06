from day6_pt1 import funcs 
import numpy as np 

with open("input.txt", "r") as file:
    input = file.read() 
task = []
lines = input.split("\n")
for l in lines:
    task.append(list(l))
task = np.array(task)

s = 0
for j in range(task.shape[1]):
    if task[-1, j] in ["*", "+"]:
        op = funcs[task[-1, j]]
        if task[-1,j] == "*": x = 1 
        if task[-1, j] == "+": x = 0
    z = "".join(task[:-1, j]).strip()
    if z == "": 
        s+= x 
    else:
        x = op(x, int(z))
s += x
print(s)