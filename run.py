from z3 import *
import time

# Schur numbers
# 1, 4, 13, 44


# not all equal
# 4, 44 => 19.02s

# a != b \/ a != c
# 4, 44 => 19.83s
 
# k = 3
# n = 14

k = 4
n = 44

s = Solver()

colors = [Int('color_%d' % i) for i in range(n)]

for i in range(n):
    s.add(And(colors[i] >= 0, colors[i] < k))
    
for a in range(1,n+1):
    for b in range(a,n+1):
        c = a + b
        if c <= n:
            # print(f"{a} + {b} = {c}")
            # not all three colors are the same
            s.add(Or(
                colors[a-1] != colors[b-1], 
                colors[a-1] != colors[c-1]
            ))
            # s.add(Not(And(
            #     colors[a-1] == colors[b-1],
            #     colors[a-1] == colors[c-1]
            # )))
            
        
            
t0 = time.time()
res = s.check()
t1 = time.time()

if res == sat:
    m = s.model()
    # print([m.evaluate(colors[i]) for i in range(n)])
    colors = [(i+1,m.evaluate(colors[i]).as_long()) for i in range(n)]
    print(f"Solution for n={n}, k={k} found in {t1-t0:.2f}s")
    # print(" ".join([str(colors[i]) for i in range(n)]))
    n_len = len(str(n))
    pad = lambda x, n: " "*(n-len(x)) + x
    print(" ".join([pad(str(i),n_len) for i, c in colors]))
    # color padded to number length
    print(" ".join([pad(str(c), n_len) for i, c in colors]))
else:
    print("No solution for n=%d, k=%d" % (n, k))
