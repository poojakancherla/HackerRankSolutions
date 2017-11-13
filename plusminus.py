n=int(input())
arr=[int(x) for x in input().split()]
zero=0.0
pos=0.0
neg=0.0
for i in arr:
    if i>0:
        pos+=1

    elif i<0:
        neg+=1
    else:
        if i==0:
            zero+=1
print(pos/n)
print(neg/n)
print(zero/n)
