# Task 1
litres = float(input("How many litres did the car use? "))
kilometres = float(input("How many kilometres has the car travelled? "))
price = float(input("How much was a litre of fuel? "))

inKm = litres / kilometres
consumption = inKm * 100

cost1km = inKm * price

print("Average fuel consumption:", consumption, "l/100km")
print("The cost of one kilometre:", cost1km, "PLN")
