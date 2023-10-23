# landscaper.py

def display_options():
    print("\nOptions:")
    print("1. Cut grass with current tool")
    print("2. Buy upgrade (if you have enough money)")
    print("3. Check balance")
    print("4. Quit game")

def buy_upgrade(tool, balance):
    tools = ["teeth", "scissors", "push lawnmower", "battery-powered lawnmower", "team"]
    costs = [0, 5, 25, 250, 500]
    earnings = [1, 5, 50, 100, 250]

    current_tool_index = tools.index(tool)

    if current_tool_index == len(tools) - 1:
        print("\nYou already have the best tool: a team of starving students!")
        return tool, balance

    cost = costs[current_tool_index + 1]

    if balance >= cost:
        balance -= cost
        tool = tools[current_tool_index + 1]
        print(f"\nCongratulations! You've just bought {tool} for ${cost}.")
    else:
        print(f"\nYou need ${cost} to buy the {tools[current_tool_index + 1]}, but you only have ${balance}.")

    return tool, balance

def cut_grass(tool, balance):
    tools = ["teeth", "scissors", "push lawnmower", "battery-powered lawnmower", "team"]
    earnings = [1, 5, 50, 100, 250]

    current_tool_index = tools.index(tool)
    earning = earnings[current_tool_index]
    balance += earning

    print(f"\nYou've earned ${earning} using your {tool}!")

    return balance

def main():
    balance = 0
    tool = "teeth"
    win_balance = 1000  # You can change this to a lower value for easier testing.

    print("Welcome to the Landscaper Game!")
    print("Start your landscaping business and earn money to buy tools and hire a team.")

    while True:
        display_options()
        choice = input("Enter your choice: ")

        if choice == "1":
            balance = cut_grass(tool, balance)
        elif choice == "2":
            tool, balance = buy_upgrade(tool, balance)
        elif choice == "3":
            print(f"\nYour current balance is ${balance}.")
        elif choice == "4":
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice. Please choose again.")

        if tool == "team" and balance >= win_balance:
            print(f"\nCongratulations! You've won the game with ${balance} in your balance and a team of starving students working for you.")
            break

if __name__ == "__main__":
    main()

