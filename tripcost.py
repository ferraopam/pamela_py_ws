#program to calculate trip cost for the given number of people
no_of_persons=int(input("Enter the no of persons:"))
distance_km=int(input("Enter the distance in KM:"))
milage_km=int(input("Enter the milage in KM:"))
fuel_price=int(input("Enter the fuel price:"))

no_liters_used=distance_km / milage_km
total_cost=no_liters_used*fuel_price
price_per_head=total_cost / no_of_persons 
print(f"Total cost per person is:{price_per_head}")
