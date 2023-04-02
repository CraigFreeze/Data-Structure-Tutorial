licensePlates = set()

def parkCar(licensePlate):
    # Parameters: License Plate
    # Call this function when a person drops off their car at the valet
    # This function should *ADD* the car's license plate to the set
    print("Car Successfully parked")
    licensePlates.add(licensePlate)

def returnCar(licensePlate):
    # Parameters: License Plate
    # Call this function when a person wants their car back from the valet
    # This function should *REMOVE* the car's license plate to the set
    print("Car Successfully Returned to Customer")
    licensePlates.remove(licensePlate)

def confirmCar(licensePlate):
    #While the car is parked, customers can come ensure that their car is still under your supervision
    if licensePlate in licensePlates:
        print("Car is safely parked!")
    else:
        print("The car is missing!")

def outputInventory():
    #Print the set to screen
    print("Here is a list of the parked cars:")
    print(licensePlates)

#There is an event going on, and many people are coming to have their cars parked
parkCar("AU421Y") # Car Successfully parked
parkCar("5DJ1368") # Car Successfully parked
parkCar("FAC080") # Car Successfully parked
parkCar("GZT6888") # Car Successfully parked
parkCar("7217TA") # Car Successfully parked
parkCar("LMM2613") # Car Successfully parked
parkCar("ASM4000") # Car Successfully parked
parkCar("16687") # Car Successfully parked

#The event is starting to end and someone is going home
returnCar("FAC080") # Car Successfully Returned to Customer

#Someone wants to confirm that their car is still there:
confirmCar("GZT6888") # Car is safely parked!

#Show which cars are leftover
outputInventory() # Here is a list of the parked cars: {'5DJ1368', 'LMM2613', 'GZT6888', 'ASM4000', '7217TA', '16687', 'AU421Y'}


