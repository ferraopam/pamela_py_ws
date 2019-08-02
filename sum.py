#program to find the sum of N natural numbers

N=int(input("Enter the value of N:"))
res=0
for ele in range(1,N+1):
    res+=ele
print(f"Sum of first {N} natural numbers is : {res}")
