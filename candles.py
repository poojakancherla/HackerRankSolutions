n=int(input())
candles=[int(x) for x in input().split()]
m=max(candles)
count=0
for i in candles:
    if i==m:
        count+=1
print(count)
