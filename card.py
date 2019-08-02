#program to find the card type using loyalty points

points=int(input("Enter the reward points:"))
if points>=0<=10000:
   card_type="Silver"
elif points>10000 and points <= 100000:
   card_type="Gold"
else:
   card_type="Platinum"
        
