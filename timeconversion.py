time=input()
new=''
if time[-2:]=='AM':
    if time[0:2]=='12':
        new='00'+time[2:-2]
        print(new)
    else:
        new=time[:-2]
        print(new)
else:
    if time[0:2]=='12':
        new=time[:-2]
    else:
        new=str(int(time[:2])+12)+time[2:-2]
    print(new)
