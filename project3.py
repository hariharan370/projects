class ParkingLot:
    def _init_(self, lanes=5, spaces_per_lane=4):
        self.lanes = lanes
        self.spaces_per_lane = spaces_per_lane
       
        self.parking = [[None for _ in range(spaces_per_lane)] for _ in range(lanes)]

    def park_vehicle(self, vehicle_number):
       
        for i in range(self.lanes):
            for j in range(self.spaces_per_lane):
                if self.parking[i][j] is None:  # Empty space found
                    self.parking[i][j] = vehicle_number
                    print(f"Vehicle {vehicle_number} parked at Lane {i+1}, Space {j+1}.")
                    return
        print("Parking Full! No space available.")

    def exit_vehicle(self, vehicle_number):
     
        for i in range(self.lanes):
            for j in range(self.spaces_per_lane):
                if self.parking[i][j] == vehicle_number:  # Vehicle found
                    self.parking[i][j] = None  # Empty the space
                    print(f"Vehicle {vehicle_number} exited from Lane {i+1}, Space {j+1}.")
                    return
        print(f"Vehicle {vehicle_number} not found in the parking lot.")

    def display_parking(self):
        """Display the current parking lot status."""
        print("\nCurrent Parking Status:")
        for i in range(self.lanes):
            print(f"Lane {i+1}: ", end="")
            for j in range(self.spaces_per_lane):
                print(self.parking[i][j] if self.parking[i][j] else "[Empty]", end="  ")
            print()
        print("-" * 40)


parking_lot = ParkingLot()


while True:
    print("\nOptions: 1. Park Vehicle  2. Exit Vehicle  3. Display Parking  4. Exit Program")
    choice = input("Enter your choice: ")

    if choice == "1":
        vehicle_number = input("Enter Vehicle Number: ")
        parking_lot.park_vehicle(vehicle_number)

    elif choice == "2":
        vehicle_number = input("Enter Vehicle Number to Exit: ")
        parking_lot.exit_vehicle(vehicle_number)

    elif choice == "3":
        parking_lot.display_parking()

    elif choice == "4":
        print("Exiting Program. Have a nice day!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
