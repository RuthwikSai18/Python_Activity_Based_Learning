#Bus Passengers
capacity = 50
passengers = 0
for i in range(5):
    n = int(input("Enter passengers: "))
    passengers += n
print("Total Passengers:", passengers)
print("Available Seats:", capacity - passengers)