def fibonocci(n):
    if(n==0):
        return[]
    elif(n==1):
        return[0]
    elif (n==2):
        return[0,1]
    l=[0,1]
    for i in range(2,n):
        l.append(l[-1]+l[-2])
    return l
num=10
print(fibonocci(num))
