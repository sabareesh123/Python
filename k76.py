#B
saj=int(input())
flag2=0
if(saj>2):
    for i in range(2,int(saj/2)+1):
        if saj%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or saj==2:
    print("no")
