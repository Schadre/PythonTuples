def calculate_average_temperature(weather_data):
    total_temp = sum(record[1] for record in weather_data)
    average_temp = total_temp / len(weather_data)
    print(f"Average Temperature: {average_temp:.2f}")

def find_highest_precipitation(weather_data):
    max_precipitation = max(weather_data, key=lambda record: record[2])
    print(f"Highest Precipitation on: {max_precipitation[0]}, Level: {max_precipitation[2]}")

def list_hot_days(weather_data):
    threshold = float(input("Enter temperature threshold: "))
    hot_days = [record for record in weather_data if record[1] > threshold] 
    for day in hot_days:
        print(f"Date: {day[0]}, Temperature: {day[1]}, Precipitation: {day[2]}")
        

def main():
    weather_data = [
        ("01/01/2020", 25.5, 5),
        ("02/01/2020", 26.7, 10),
        ("03/01/2020", 24.8, 7)
    ]

    while True:
        print("\n1. Calculate Average Temperature")
        print("2. Find Highest Precipitation")
        print("3. List Hot Days")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_average_temperature(weather_data)
        elif choice == "2":
            find_highest_precipitation(weather_data)
        elif choice == "3":
            list_hot_days(weather_data)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()