from social_network_classes import SocialNetwork
import social_network_ui

ai_social_network = SocialNetwork()

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")

    choice = social_network_ui.main_menu()

    while True:
        if choice == "1":
            print("\nYou are now in the create account menu")
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            ai_social_network.create_account(name, age)

        elif choice == "2":
            inner_menu_choice = social_network_ui.manage_account_menu()
            while True:
                if inner_menu_choice == "5":
                    break
                elif inner_menu_choice == "2":
                    person_name = input("Enter your name: ")
                    friend_name = input("Enter friend's name: ")
                    ai_social_network.add_friend(person_name, friend_name)
                    break
                elif inner_menu_choice == "4":
                    person_name = input("Enter your name: ")
                    for person in ai_social_network.list_of_people:
                        if person.name == person_name:
                            print(f"Messages for {person_name}:")
                            for message in person.messages:
                                sender, msg = message
                                print(f"From {sender}: {msg}")
                            break
                    else:
                        print("Person not found.")
                else:
                    inner_menu_choice = social_network_ui.manage_account_menu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        choice = social_network_ui.main_menu()