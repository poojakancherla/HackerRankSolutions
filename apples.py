s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())


pos_m=0
pos_n=0


dist_a = [int(x) for x in input().split()]
dist_b = [int(x) for x in input().split()]

for i in dist_a:
    if i>0:
        if a+i>=s and a+i<=t:
            pos_m+=1
for j in dist_b:
    if j<0:
        if b+j>=s and b+j<=t:
            pos_n+=1

print(pos_m)
print(pos_n)
