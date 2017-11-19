n, s = map(int, input().split())
sv = {}
for i in range(n):
    sv[i] = i
for j in range(s):
    # print(sv)
    a, b = map(int, input().split())
    summ = 0
    for i in range(a, b+1):
        if i in sv.keys():
            summ += sv[i]
            del sv[i]
    l = -1
    r = -1
    for i in range(a-1, -1, -1):
        if i in sv.keys():
            l = i
            break
    try:
        summ += sv[l]
        del sv[l]
    except:
        pass

    for i in range(b+1, n):
        if i in sv.keys():
            r = i
            break
    try:
        summ += sv[r]
        del sv[r]
    except:
        pass
    print(summ)
