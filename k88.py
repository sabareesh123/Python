import sys, string, math
j,b = map(int,input().split())
for i in range(max(j,b),j*b+1) :
    if (i%j == 0) and ( i%b == 0) :
        lcm = i
        break
print(lcm)
