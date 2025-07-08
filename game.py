def start_game():
    print("Welcome to 'The Airport Trap' - A Cybersecurity Awareness Game!")
    print("You're Gwen, a financial worker waiting at the airport for your flight.")
    print("You see a Wi-Fi network named 'Free Airport Wi-Fi'.")
    choice1 = input("Do you connect to it? (yes/no): ").strip().lower()

    if choice1 == "yes":
        print("\nYou connect to the network. It seems to work fine.")
        print("You decide to log into the company's bank account to make a quick transaction.")
        choice2 = input("Do you use a VPN before logging in? (yes/no): ").strip().lower()

        if choice2 == "yes":
            print("\nSmart move! Your VPN encrypts your traffic.")
            print("Even if someone is snooping, they can't see your data.")
            print("You safely access your company's bank account and log out. Well done!")
        else:
            print("\nOh no! A hacker is monitoring the network.")
            print("They capture your login credentials and access your company's bank account.")
            print("Your manager later notices the money missing from the bank account.")
            print("Lesson: Always use a VPN on public Wi-Fi!")
    elif choice1 == "no":
        print("\nGood choice! You avoid the suspicious network.")
        print("You use your mobile hotspot instead and securely access your company's bank account.")
        print("Your company's finances remain safe. Great job!")
    else:
        print("\nInvalid input. Please restart the game and type 'yes' or 'no'.")

# Run the game
start_game()
