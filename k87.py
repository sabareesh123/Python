import sys, string, math
j,b = map(int,input().split())
for i in range(1, min(j,b)+1) :
    if (j%i == 0) and ( b%i == 0) : gcd = i
print(gcd)
