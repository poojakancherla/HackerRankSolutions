t = int(input())
z = [0]
for i in range(1, t+1):
    string = input()
    z.append(string)

q = int(input())

for j in range(q):
    new_s = []
    new_z = []
    l, r, s = input().strip().split(' ')
    l, r, s = [int(l), int(r), str(s)]
    count = 0
    for i in range(l,r+1):
        new_s.append(0)
        new_z.append(0)
    for i in range(l, r+1):
        if len(z[i])<=len(s):
            new_s = (s[:len(z[i])])
            if(z[i]<=new_s):
                count+=1

        else:
            if len(z[i])>=len(s):
                new_z[i]=(z[i][:len(s)])
                if(s<=new_z[i]):
                    count+=1
                    

    print(count)
