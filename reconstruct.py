import os
import sys

# space separated ids with no sign or -
sol_file="schur_160_5_sol.txt"
# per line name and id separated by space
mapping="schur_160_5.var_mapping"

sign = {}
with open(sol_file, "r") as f:
    for part in f.read().split():
        if part[0] == "-":
            sign[part[1:]] = False
        else:
            sign[part] = True
map = {}
with open(mapping, "r") as f:
    for line in f:
        name, id = line.strip().split()
        map[id] = name
        
sign_vars = set(sign.keys())
map_vars = set(map.keys())

# all vars that are in the solution but not in the mapping
diff = sign_vars - map_vars
if diff:
    print("Warning: vars in solution but not in mapping: ", diff)
# all vars that are in the mapping but not in the solution
diff = map_vars - sign_vars
if diff:
    print("Warning: vars in mapping but not in solution: ", diff)

# reconstruct which names are true and not
true_vars = set()
for id, val in sign.items():
    if val and id in map:
        true_vars.add(map[id])

for num in range(160):
    for c in range(5):
        if f"color_{num}_{c}" in true_vars:
            print(f"{num} {c}")
