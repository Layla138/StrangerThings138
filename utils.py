# utils.py

def print_intro():
    print(r"      ':.")
    print(r'         []_____ Victor Creel')
    print(r'        /\      \\  House')
    print(r'    ___/  \__/\__\__')
    print(r"---/\___\ |''''''|__\-- ---")
    print(r"   ||'''| |''||''|''|")
    print(r'   ``"""`"`""))""`""`')


def get_user_input(prompt, choices):
    print('\n' + prompt + '\n')
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    user_input = input("\nEnter the number of your choice: ").strip()

    if user_input.isnumeric() and int(user_input) in range(1, len(choices) + 1):
        print('\n')
        return int(user_input) - 1
    else:
        print("Invalid choice. Please try again.")
        return get_user_input(prompt, choices)

def fight(enemy_name):
    player_health = 100
    enemy_health = 100

    print(f"You are fighting {enemy_name}!")

    while player_health > 0 and enemy_health > 0:
        prompt = f"\nYour Health: {player_health}\n{enemy_name}'s Health: {enemy_health}\n\nWhat attack do you choose?"
        choices = ["Fire Ball", "Wizard Blast"]

        choice = get_user_input(prompt, choices)

        if choice == 0:
            enemy_health -= 50
            print(f"You hit {enemy_name} with a Fire Ball! {enemy_name} loses 50 health.(Good Ending 😁👍)")
        elif choice == 1:
            enemy_health -= 70
            print(f"You hit {enemy_name} with a Wizard Blast! {enemy_name} loses 70 health.")
        else:
            print("Invalid choice. Please try again.")

        if enemy_health <= 0:
            print(f"You defeated {enemy_name}!\n\nYou won the game!(Good Ending 😁👍)")
        else:
            player_health -= 30
            print(f"{enemy_name} attacks you! You lose 30 health.")

            if player_health <= 0:
                print(f"{enemy_name} defeated you.\n\nGame Over.")
                break
