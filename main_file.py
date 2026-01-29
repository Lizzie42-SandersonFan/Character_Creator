import random
import sys
import time

def slow_print(text, delay=0.1):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

classes = { 
1 : {"Name": "Fighter", "Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}},
2 : {"Name": "Rogue", "Weapons": ["Daggers", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}},
3 : {"Name": "Cleric", "Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}}}

characters = []

def main_menu():
    """
    Displays the main menu options for the player.
    """
    options = {
        1: "View Character",
        2: "Create Character",
        3: "Edit Character",
        4: "Leave Game"
    }

    print("\nMain Menu")
    for key, value in options.items():
        print(f"{key}. {value}")
def menu():
    print("Main Menu")
    print("1. View Characters")
    print("2. Create Character")
    print("3. Edit Character")
    print("4. Exit")
    menu_option = input("Select an option (1-4): ")
    if menu_option == "1":
        view_characters()
    elif menu_option == "2":
        create_character()
    elif menu_option == "3":
        edit_character()
    elif menu_option == "4":
        exit()
    else:
        print("Invalid option. Please try again.")

def create_character():
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
    slow_print("You have two empty stats.")
    print("Rolling for your stats...")  
    #generator random stats
    character["Stats"]["Dexterity"] = random.randint(10, 30)
    character["Stats"]["Intelligence"] = random.randint(10, 30)
    #Display rolled stats
    slow_print(f"Your rolled stats are: Dexterity: {character['Stats']['Dexterity']}, Intelligence: {character['Stats']['Intelligence']}")
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
    slow_print(f"Character created:\nName: {character['Name']}\n Class: {character['Class']}\n Stats:\n Strength: {character['Stats']['Strength']}\n Health: {character['Stats']['Health']}\n Wisdom: {character['Stats']['Wisdom']}\n Dexterity: {character['Stats']['Dexterity']}\n Intelligence: {character['Stats']['Intelligence']}\n XP: {character['XP']}\n Level: {character['Level']}\n Weapon: {character['Weapon']}")
def main():
    #Main program loop
    while True:
        #Run Character Creation
        create_character()
        #Ask if user wants to create another character
        another = input("Do you want to create another character? (yes/no): ")
        if another.lower() != 'yes':
            break
main()
def create_character():
    character = {}
    character['name'] = input("Enter your character's name: ")
    print("Choose your class:")
    print("1. Rogue")
    print("2. Cleric")
    class_choice = input("Enter the number of your choice: ")
    
    if class_choice == '1':
        character['class'] = 'Rogue'
        character['strength'] = 20
        character['health'] = 20
        character['wisdom'] = 20
        character['xp'] = 0
        character['level'] = 1
    elif class_choice == '2':
        character['class'] = 'Cleric'
        character['strength'] = 10
        character['health'] = 30
        character['wisdom'] = 20
        character['xp'] = 0
        character['level'] = 1
    else:
        print("Invalid choice. Please try again.")
        return create_character()
    
    return character
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