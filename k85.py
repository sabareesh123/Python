import sys, string, math
j = input()
j1 = ''
j2 = ''
for i in range(len(j)) :
    if i%2 == 0 : j1 += j[i]
    else :        j2 += j[i]
print(j1,j2)
