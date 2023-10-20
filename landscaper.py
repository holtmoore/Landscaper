# landscaper.py

def display_options():
    print("\nOptions:")
    print("1. Cut grass with teeth")
    print("2. Check balance")
    print("3. Quit game")

def cut_grass_with_teeth(balance):
    earning = 1
    balance += earning
    print(f"\nYou've earned ${earning} using your teeth!")
    return balance

def main():
    balance = 0

    print("Welcome to the Landscaper Game!")
    print("Start your landscaping business with just your teeth.")

    while True:
        display_options()
        choice = input("Enter your choice: ")

        if choice == "1":
            balance = cut_grass_with_teeth(balance)
        elif choice == "2":
            print(f"\nYour current balance is ${balance}.")
        elif choice == "3":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice. Please choose again.")

if __name__ == "__main__":
    main()
