mee=int(input())
fl=0
if mee>2:
    for i in range(3,int(mee/2)):
        if mee%i==0:
            fl=1
            print("no")
            break
if fl==0 or mee==2:
    print("yes")
