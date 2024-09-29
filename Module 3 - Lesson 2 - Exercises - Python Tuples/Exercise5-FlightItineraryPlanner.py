def display_itineraries(itineraries):
    for itinerary in itineraries:
        traveler, flights = itinerary[0], itinerary[1:]
        print(f"\nTraveler: {traveler}")
        for flight in flights:
            print(f"  Flight: {flight[0]}, From: {flight[1]}, To: {flight[2]}")

def find_itinerary_by_traveler(itineraries, traveler_name):
    for itinerary in itineraries:
        if itinerary[0].lower() == traveler_name.lower():
            print(f"\nItinerary for {traveler_name}: ")
            for flight in itinerary[1:]:
                print(f"Flight: {flight[0]}, From: {flight[1]}, To: {flight[2]}")
            break
    else:
        print("No itinerary found for this traveler.")

def list_itineraries_from_city(itineraries, city):
    print(f"\nItineraries from {city}: ")
    for itinerary in itineraries:
        for flight in itinerary[1:]:
            if flight[1].lower() == city.lower():
                print(f"Traveler: {itinerary[0]}, Flight: {flight[0]}, To: {flight[2]}")


def main():
    itineraries = [
        ("Alice", ("FL123", "New York", "London"), ("FL456", "London", "Paris")),
        ("Bob", ("FL789", "Tokyo", "San Francisco"), ("FL321", "San Francisco", "New York")),
    ]

    while True:
        print("\n1. View all itineraries")
        print("2. Search itinerary by traveler")
        print("3. List itineraries from a city")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_itineraries(itineraries)
        elif choice == "2":
            traveler = input("Enter traveler's name: ")
            find_itinerary_by_traveler(itineraries, traveler)
        elif choice == "3":
            city = input("Enter departure city: ")
            list_itineraries_from_city(itineraries, city)
        elif choice == "4":
            print("Exiting program.")
            break 
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()