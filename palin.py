#program to detemine whether the entered number is palindrome or not

num = int(input("Enter a number:"))
tnum = num
rev = 0
while tnum != 0:
    r = tnum % 10
    rev = rev * 10 + r
    tnum = tnum // 10
if num == rev:
    print(f"entered {num} is a palindrome")
else:
    print(f"entered {num} is not a palindrome")