#program to find number divisible by 3,6 but not 9

N = int(input("Enter the value of N:"))
c = 0
i = 1
while True:
    if i % 3 == 0 and i % 6 == 0 and not i % 9 == 0:
        print(i,end=" ")
        c+=1
    if c == N:
            break
    i+=1