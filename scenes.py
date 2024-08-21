# scenes.py

from utils import get_user_input, fight

def scene_one():
    prompt = "You find yourself in The UpsideDown.\n\nWhat do you do?"
    choices = ["Explore", "Sneak into Vecna's Lair", "Shout for help", "Find The Hawkins Lab"]

    choice = get_user_input(prompt, choices)

    if choice == 0:
        scene_two()
    elif choice == 1:
        scene_sneaking_in()
    elif choice == 2:
        print("No one hears you...\n\nGame Over.(Decent ending 😶)")
    elif choice == 3:
        scene_four()

def scene_sneaking_in():
    prompt = "You walk in and the door slams shut behind you… And Vecna says 'Join me..'\n\nWhat do you do?"
    choices = ["Fight", "Retreat Safely", "Join Vecna"]

    choice = get_user_input(prompt, choices)

    if choice == 0:
        fight("Vecna")
    elif choice == 1:
        print("You retreat safely!\n\nYou won the game!(Good Ending😁👍)")
    else:
        print("You join Vecna and cause trouble for Hawkins...\n\nGame Over..(Bad Ending😬)")

def scene_two():
    prompt = "You are exploring and you get spotted by the Demogorgon!\n\nWhat do you do?"
    choices = ["Fight", "Retreat Safely"]

    choice = get_user_input(prompt, choices)

    if choice == 0:
        fight("Demogorgon")
    elif choice == 1:
        print("You retreat safely!\n\nYou won the game!(Good ending 😁👍)")

def scene_four():
    prompt = "You find the Hawkins Lab.\n\nWhat do you do?"
    choices = ["Enter the Hawkins Lab", "Continue exploring The UpsideDown"]

    choice = get_user_input(prompt, choices)

    if choice == 0:
        scene_hidden_passage()
    elif choice == 1:
        scene_five()

def scene_hidden_passage():
    prompt = "You enter the Hawkins Lab and find a strange portal...\n\nWhat do you do?"
    choices = ["Go in the portal", "Leave the portal and continue exploring"]

    choice = get_user_input(prompt, choices)

    if choice == 0:
        print("You go in the portal. It transported you back to the real world!\n\nYou won the game!(Good Ending 😁👍)")
    elif choice == 1:
        print("You leave the portal alone and continue exploring and nothing happened.\n\nGame over (Decent ending😶)")
        # Add code to handle the new challenge

def scene_five():
    prompt = "You continue exploring The Upside Down.\n\nWhat do you do?"
    choices = ["Look for a place to stay for a while", "Try to find a way out of the Upside Down"]

    choice = get_user_input(prompt, choices)

    if choice == 0:
        print("You find a shelter and stay there...\n\nThen you continue your journey!(Decent ending 😶)")
        # Add code to handle the next scene
    elif choice == 1:
        print("You try to escape the Upside Down, but fail.\n\nYou attract unwanted attention...(Bad ending 😬)")
        fight("Demogorgans")
        # Add code to handle the consequences of attracting attention
