#B
saj=input()
n2=len(saj)
if n2%2!=0:
    saj=saj[:int(n2/2)]+'*'+saj[int(n2/2)+1:n2]
else:
    saj=saj[:int(n2/2)-1]+'**'+saj[int(n2/2)+1:n2]
print(saj)
