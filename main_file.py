# LD, LV, & TE First gorup Project
import random
import sys
import time

def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

classes = { 
1 : {"Name": "Fighter", "Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}},
2 : {"Name": "Rogue", "Weapons": ["Daggers", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}},
3 : {"Name": "Cleric", "Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}}}

characters = []

def menu():
    while True:
        print("Main Menu")
        print("1. View Characters")
        print("2. Create Character")
        print("3. Edit Character")
        print("4. Exit")
        menu_option = input("Select an option (1-4): ")
        if menu_option == "1":
            view_character()
        elif menu_option == "2":
            create_character()
        elif menu_option == "3":
            edit_character()
        elif menu_option == "4":
            exit()
        else:
            print("Invalid option. Please try again.")
            continue

def create_character():
    def main():
        #Main program loop
        while True:
        #Run Character Creation
            #Ask if user wants to create another character
            another = input("Do you want to create another character? (yes/no): ").strip()
            if another.lower() != 'yes':
                break
            else:
                create_character()

    #For each class in class options
    for key, value in classes.items():
        print(f"{key}: {value['Name']}:{value['Stats']}")

    #Try and except
    try:
    #Class is set to input type 1-3 to choose your class
        c_class = int(input("Enter the number of your class choice: "))
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your class choice.")
        return

    #If choice is invalid, stop function
    if c_class not in classes:
        print("Invalid class choice.")
        return       

    #Get select class data
    base_class = classes[c_class]
    #Copy base stats so originial class stats are not changed
    character = { "Class": base_class["Name"], "Stats": base_class["Stats"].copy(), "Weapon": None }
    #Inform user about random stats
    type_print("You have two empty stats.\n")
    print("Rolling for your stats...")  
    time.sleep(0.5)
    #generator random stats
    character["Stats"]["Dexterity"] = random.randint(10, 30)
    character["Stats"]["Intelligence"] = random.randint(10, 30)
    #Display rolled stats
    type_print(f"Your rolled stats are: Dexterity: {character['Stats']['Dexterity']}, Intelligence: {character['Stats']['Intelligence']}\n")
    #Ask user to choose a weapon
    print("Choose your weapon from the following options:")
    #For i in weapons
    for i, weapon in enumerate(base_class["Weapons"], 1):
        #Print weapon options
        print(f"{i}: {weapon}")
        #Try and accept weapon choice
    try:
        weapon_choice = int(input("Enter the number of your weapon choice: "))
        #If weapon choice is valid, set weapon
        if 1 <= weapon_choice <= len(base_class["Weapons"]):
            #Set character weapon
            character["Weapon"] = base_class["Weapons"][weapon_choice - 1]
            #Else invalid weapon choice
        else:
            print("Invalid weapon choice.")
            return
        #Catch value error
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your weapon choice.")
        return
    #Add xp and level to char dict.
    character["XP"] = 0
    character["Level"] = 1
    #Name character
    character["Name"] = input("Enter your character's name: ")
    #Finish character creation
    characters.append(character)
    type_print(f"Character created:\nName: {character['Name']}\n Class: {character['Class']}\nStats:\n Strength: {character['Stats']['Strength']}\n Health: {character['Stats']['Health']}\n Wisdom: {character['Stats']['Wisdom']}\n Dexterity: {character['Stats']['Dexterity']}\n Intelligence: {character['Stats']['Intelligence']}\nXP: {character['XP']}\nLevel: {character['Level']}\nWeapon: {character['Weapon']}\n")
    main()


def level_up_loop(character):
    """
    Checks if the character has enough XP to level up.
    Rogue needs 15 XP per level.
    Cleric needs 20 XP per level.
    """
    if character['class'] == 'Rogue':
        xp_needed = character['level'] * 15
    else:
        xp_needed = character['level'] * 20

    if character['xp'] >= xp_needed:
        character['xp'] -= xp_needed
        character['level'] += 1
        character['strength'] += 1

    if character['class'] == 'Cleric' and character['level'] % 5 == 0:
        character['spell_slots'] += 1
        print("You gained an extra spell slot!")

        print(f"{character['name']} leveled up to level {character['level']}!")
    else:
         return
    
def view_character():
    global characters
    if not characters:
        type_print("You don't have any characters to view.\nRedirecting you to main menu to make a character\n")
        menu()
    else:
        type_print("These are the characters you have to view\n")
        for character in characters:
            print(f"{character['Name']}: {character["Class"]}): Level {character["Level"]}")
        print("Leave")
    
    # Get user to acctually select a chracter to view
    while True:
        view_choice = input("Type the name of the character you want to view (or 'Leave' if you want to go back to main menu):\n").strip()
        if view_choice == "Leave":
            type_print("Redirecting to main menu . . .\n")
            time.sleep(0.5)
            menu()
            break
        for chara in characters:
            if view_choice == chara["Name"]:
                type_print(f"Viewing Character:\n Name: {chara['Name']}\n Class: {chara['Class']}\nStats:\n Strength: {chara['Stats']['Strength']}\n Health: {chara['Stats']['Health']}\n Wisdom: {chara['Stats']['Wisdom']}\n Dexterity: {chara['Stats']['Dexterity']}\n Intelligence: {chara['Stats']['Intelligence']}\nLevel: {chara['Level']}\nXP: {chara['XP']}\nWeapon: {chara['Weapon']}\n")
                while True:
                    type_print("Would you like to\n1) View another character\nor\n2) Go back to main menu\n")
                    again = input("Type the number for the action you would like to do\n")
                    if again == "1":
                        view_character()
                        break
                    elif again == "2":
                        type_print("Redirecting to main menu . . .\n")
                        time.sleep(0.5)
                        menu()
                        break
                    else:
                        print("Invalid input. Try again")
                        continue
            else:
                continue
            print("Could not find the character you typed in. Check your spelling and punctuation.")
            continue

def edit_character():
    def edit_XP():
        # Helper to add/remove. Have user type in number to add/remove. Update XP
        adding = adding_removing("XP")
        if adding == "ADDING":
            while True:
                type_print("How much XP would you like to add to your character?\n")
                add = input("This needs to be a whole number\n").strip().upper()
                if check_valid_num(add) == True:
                    return int(add)
                else:
                    print("You seemed to have entered an invalid number. Please try again")
                    continue
        else:
            while True:
                type_print("How much XP would you like to remove from your character?\n")
                remove = input("This needs to be a whole number\n").strip().upper()
                if check_valid_num(remove) == True:
                    return int(remove)
                else:
                    continue

    def edit_stat():
        # Have user select stat to reroll. Reroll with random number and save it
        while True:
            # i need to display the list of stats and have the user pick the stat. I will choose a random number between 10 and 30 and return the stat picked AND the new value
            type_print("Which stat would you like to reroll:\nStrength\nWisdom\nDexterity\nIntelligence\n")
            choice = input("Type the NAME of the stat you would like to reroll\n").strip().title()
            if choice == "Strength":
                new_value = random.randint(10, 30)
                return choice, new_value
            elif choice == "Wisdom":
                new_value = random.randint(10, 30)
                return choice, new_value
            elif choice == "Dexterity":
                new_value = random.randint(10, 30)
                return choice, new_value
            elif choice == "Intelligence":
                new_value = random.randint(10, 30)
                return choice, new_value
            else:
                print("Invalid input. Try again")
                continue

    def edit_invintory():
        # Use helper to know if adding or removing. Have user type in something to add\remove to invintory list
        adding = adding_removing("invintory")
        if adding == "ADDING":
            while True:
                add = input("What would you like to add to your character's invintory\n").strip().title()
                # I need True to set up an invintory so I can append 'add' into it 
        else:
            while True:
                remove = input("What would you like to remove from your character's invintory\n").strip().title()
                # True needs to give me an invintory so I can hunt down 'remove' and remove it from the list

    def adding_removing(thing):
        # Helper function that will ask the user if they are adding or removing
        while True:
            type_print(f"Are you adding to {thing} or removing from {thing}\n")
            a_r = input("Enter 'ADDING' if adding or 'REMOVING' if removing\n").strip().upper()
            if a_r == "ADDING":
                return "ADDING"
            elif a_r == "REMOVING":
                return "REMOVING"
            else:
                print("Invalid input. Please try again")
                continue
    
    def check_valid_num(num):
        if num.isdigit() == True:
            if int(num) % 1 == 0:
                # User gave a valid number
                return True
            else:
                print("You seemed to have entered a number, but it's not a whole number. Try again")
        else:
            print("You seemed to have entered something other than a number. Try again")

    global characters
    if not characters:
        type_print("You don't have any characters to edit.\nRedirecting you to main menu to make a character\n")
        menu()
    else:
        while True:
            type_print("These are the characters you have to edit:\n")
            for character in characters:
                # Print the character names with a number before each one
                print(f"{character['Name']} ({character["Class"]})")
            print("Leave")
            edit_choice = input("Type the name of the character you want to edit (or 'Leave' if you want to go back to main menu):\n").strip()
            if edit_choice == "Leave":
                type_print("Redirecting to main menu . . .\n")
                time.sleep(0.5)
                menu()
                break
            for chara in characters:
                if edit_choice == chara["Name"]: 
                    # Now give the user a list of things to edit and call the inner function corresponding to the selection
                    while True:
                        type_print(f"What would you like to edit on {chara["Name"]}:\n1) XP amount\n2) Reroll a stat\n3) {chara["Name"]}'s Invintory\n")
                        choice = input("Type the number corresponding to what you want to edit\n").strip().upper()
                        if choice == "1":
                            xp = edit_XP()
                            type_print(f"Ajusting XP . . .\n")
                            time.sleep(0.5)
                            chara["XP"] += xp
                            type_print("XP updated\n")
                            type_print(f"XP for {chara["Name"]} is {chara['XP']}\n")
                            level_up_loop()
                            break
                        elif choice == "2":
                            stat, value = edit_stat()
                            type_print(f"Your new stat for {stat} is {value}\n")
                            chara[stat] = value
                            break
                        elif choice == "3":
                            #item = edit_invintory()
                            print("Unable to edit invintory right now. Please pick something else to edit\n")
                            continue
                    # We have left the editing loop and now need to leave the selection loop
                    type_print(f"Would you like to:\n1) continue editing characters or\n2) Leave\n")
                    stay = input("Type the number corresponding to the action you would like to do\n")
                    if stay == "1":
                        continue
                    else:
                        type_print("Leaving character editor.\nRedirecting to main menu . . .\n")
                        menu()
                else:
                    print("Could not find the character you typed in. Check your spelling and punctuation.")
                    continue

menu()