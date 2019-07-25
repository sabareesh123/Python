from itertools import combinations
(j,x) =input().split()
x=int(x)
arr=[]
comb=combinations(j,len(j)-x)
comb=list(comb)

for i in (comb):
    arr.append("".join(i))

print(min(arr))
