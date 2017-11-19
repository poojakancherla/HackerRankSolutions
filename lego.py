t=int(input())
l=[]
for i in range(t):
    l = list(map(int, input().split()))
    p,q = map(int, input().split())
    # l.append(a,b,c,d)
    if p in l:
        l.remove(p)
    if q in l:
        l.remove(q)
    print(l[0]*l[1])
