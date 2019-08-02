#program to find series of armstrong numbers

N=int(input("Enter the value of N:"))
i=1
c=0
while True:
    num=i
    res=0
    while num!=0:
        res+=((num%10) ** 3)
        num //= 10
    if i==res:
        print(i)
        c+=1
    i+=1
    if c==N:
        break