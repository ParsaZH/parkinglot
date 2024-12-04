import datetime

parking_lot = {}

def enter_parking():
    car_plate_number = input("Enter car plate number: ")
    if car_plate_number in parking_lot:
        print("This car is already in the parking lot.")
        return
    entry_time = datetime.datetime.now()
    parking_lot[car_plate_number] = [{"entry_time": entry_time, "exit_time": None}]
    print(f"Car with plate number {car_plate_number} has entered the parking lot at {entry_time}.")

def exit_parking():
    car_plate_number = input("Enter car plate number: ")
    if car_plate_number not in parking_lot or parking_lot[car_plate_number][-1]["exit_time"] is not None:
        print("Car not found in the parking lot or it's already exited.")
        return
    
    entry_time = parking_lot[car_plate_number][-1]["entry_time"]
    
    exit_time = datetime.datetime.now()
    time_spent = exit_time - entry_time
    hours_spent = time_spent.total_seconds() // 3600
    
    fee = 5000  
    if hours_spent > 6:
        extra_hours = hours_spent - 6
        fee += extra_hours * 1000  
    
    parking_lot[car_plate_number][-1]["exit_time"] = exit_time
    
    print(f"Car with plate number {car_plate_number} has exited the parking lot.")
    print(f"Time spent: {time_spent}")
    print(f"Parking fee: {fee} Tooman.")

def view_parking_status():
    if not parking_lot:
        print("The parking lot is empty.")
    else:
        print("Current cars in the parking lot:")
        for plate_number, sessions in parking_lot.items():
            print(f"\nCar {plate_number}:")
            for session in sessions:
                entry_time = session["entry_time"]
                exit_time = session["exit_time"]
                if exit_time is None:
                    print(f"  - Entered at {entry_time} and is currently in the parking lot.")
                else:
                    time_spent = exit_time - entry_time
                    print(f"  - Entered at {entry_time}, exited at {exit_time}, time spent: {time_spent}")

def main():
    while True:
        print("\nParking Management System")
        print("1. Enter Parking")
        print("2. Exit Parking")
        print("3. View Parking Status")
        print("4. Exit Program")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            enter_parking()  
        elif choice == "2":
            exit_parking() 
        elif choice == "3":
            view_parking_status() 
        elif choice == "4":
            print("Exiting program.")
            break 
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  
