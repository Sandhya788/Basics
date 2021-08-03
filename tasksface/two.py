a=input()
esum=int(0)
osum=int(0)
for i in range(0,len(a)):
    if i%2==0:
        esum+=int(a[i])
    else:
        osum+=int(a[i])
print(int(abs(esum-osum)))
