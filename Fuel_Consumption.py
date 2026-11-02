#Fuel consumption
distance = int(input("Enter distance: "))
vehicles = [15, 20, 25]
for i in range(3):
    fuel = distance / vehicles[i]
    cost = fuel * 100
    print("Vehicle", i + 1)
    print("Fuel:", fuel)
    print("Cost:", cost)