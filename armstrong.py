#program to check whether the given number is armstrong

num=int(input("Enter the number:"))
sum=0
tnum= num
while num!=0:
    r=num%10
    sum=sum+ r**3
    num=num // 10
if tnum==sum:
        print(f"given number is armstrong")
else:
    print(f"given number is not armstrong")