import sys, string, math
j = input()
k = j.count(j[0])
flag = 1
for i in range(1,len(j)) :
    if j.count(j[i]) != k :
        flag = 0
        break
if flag : print('Yes')
else : print('No')
