import csv

class Vehicle:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def print(self):
        print(f"Year:  {self.year}")
        print(f"Make:  {self.make}")
        print(f"Model: {self.model}\n")

# car1 = vehicle(2012, "Mercedes", "C300")
# car1.print()

# Open file
inv_file = open("inventory.txt", "r") # The r specifies the access (r being read-only, I think)
file_path = "inventory.txt"

# Create a list to store the vehicle objects
inventory = []

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) # This line would skip the header row
    for row in csvreader:
        year, make, model = row # This will upack the row directly into variables
        
        # Now we can create a vehicle object and store it in the list
        car = Vehicle(year, make, model)
        
        # Then we simply append the newly created vehicle object to the list
        inventory.append(car)
        
# Now we can iterate through the list and call the vehicle print member function
for car in inventory:
    car.print()

inv_file.close()

