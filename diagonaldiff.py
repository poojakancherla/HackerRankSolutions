n=int(input())
a=[]
forward=0
reverse=0
for i in range(n):
    at = [int(x) for x in input().split()]
    a.append(at)
x, y = 0, 0
for j in range(n):
    x += a[j][j]
    y += a[j][len(a)-j-1]
print(abs(x-y))
