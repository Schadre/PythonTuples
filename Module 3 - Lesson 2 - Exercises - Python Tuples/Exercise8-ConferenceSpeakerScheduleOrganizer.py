def display_schedule(schedule):
    for day, sessions in schedule.items():
        print(f"\n{day}:")
        for session in sessions:
            print(f" - Title: {session[0]}, Speaker: {session[1]}")


def repeat_session(schedule, day):
    session_title = input("Enter the title of the session to repeat: ")
    for session in schedule[day]:
        if session[0].lower() == session_title.lower():
            schedule[day] = schedule[day] + (session,)
            print(f"Session '{session_title}' repeated.")
            return 
    print("Session not found")

def check_speaker(schedule):
    speaker_name = input("Enter the speaker's name to check: ")
    for day, sessions in schedule.items():
        if any(speaker_name.lower() in session[1].lower() for session in sessions):
            print(f"{speaker_name} is presenting on {day}.")
            return 
    print(f"{speaker_name} is not presenting.")


def main():
    schedule = {
        "Day 1": (("Opening Keynote", "Alice Johnson"), ("Python Workshop", "Bob Smith")),
        "Day 2": (("AI Panel", "Charlie Davis"), ("Closing Remarks", "Alice Johnson")),
    }

    while True:
        print("\n1. View conference schedule")
        print("2. Repeat a session")
        print("3. Check if a speaking is presenting")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_schedule(schedule)
        elif choice == "2":
            day = input("Enter the day to repeat a session: ")
            if day in schedule:
                repeat_session(schedule, day)
            else:
                print("Invalid day.")
        elif choice == "3":
            check_speaker(schedule)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()