n=[int(x) for x in input().split()]
s=sorted(n)
max=0
min=0
for i in range(1,5):
    max+=s[i]
for i in range(0,4):
    min+=s[i]
print(min,max)
