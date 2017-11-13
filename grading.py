n=int(input())

for i in range(n):
    rounded=0
    marks=int(input())
    if marks+3<40:
        rounded=marks
    else:
        quo=int((marks/5))+1
        if ((5*quo)-marks)<3:
            rounded=5*quo
        else:
            rounded=marks
    print(rounded)
