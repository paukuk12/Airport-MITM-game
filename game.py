
def start_game():
    print("Welcome to 'The Airport Trap' - A Cybersecurity Awareness Game!")
    print("You're Alex, a tech executive waiting at the airport for your flight.")
    print("You see a Wi-Fi network named 'Free Airport Wi-Fi'.")
    choice1 = input("Do you connect to it? (yes/no): ").strip().lower()

    if choice1 == "yes":
        print("\nYou connect to the network. It seems to work fine.")
        print("You decide to check your company dashboard.")
        choice2 = input("Do you use a VPN before logging in? (yes/no): ").strip().lower()

        if choice2 == "yes":
            print("\nSmart move! Your VPN encrypts your traffic.")
            print("Even if someone is snooping, they can't see your data.")
            print("You safely access your dashboard and log out. Well done!")
        else:
            print("\nOh no! A hacker is monitoring the network.")
            print("They capture your login credentials and access your company data.")
            print("Your IT team later detects suspicious activity from a foreign IP.")
            print("Lesson: Always use a VPN on public Wi-Fi!")
    elif choice1 == "no":
        print("\nGood choice! You avoid the suspicious network.")
        print("You use your mobile hotspot instead and securely access your dashboard.")
        print("Your data remains safe. Great job!")
    else:
        print("\nInvalid input. Please restart the game and type 'yes' or 'no'.")

# Run the game
start_game()
