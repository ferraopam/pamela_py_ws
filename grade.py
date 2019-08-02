#program to find the grade

sub1 = int(input("Enter the marks in subject 1:"))
sub2 = int(input("Ener the marks in subject 2:"))
sub3 = int(input("Enter te marks in subject 3:"))
if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    avg = (sub1 + sub2 + sub3) / 3
    if avg >= 35 and avg <= 65:
        print(f"Grade: C")
    if avg > 65 and avg <= 85:
        print(f"Grade: B")
    if avg > 85 and avg <= 100:
        print(f"Grade: C")
    Selse:
       print(f"Something really went wrong...")
else:
   print(f"Sorry!Better luck next time...")

