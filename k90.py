import sys, string, math
j = input()
L = []
for c in j :
    if c.isdigit() : L.append(c)
print(*L,sep='')
