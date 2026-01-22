#TE 2nd Character Creator
#Import Random
import random

#List for character weapons
#Fighter Dictionary: Weapons: Greatsword, Greataxe, Maul. Stats: Strength: 30, Health: 20, Wisdom: 10.
fighter_info = {"Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10.}}
#Rogue Dictionary: Weapons: Dagger, Blowgun, Knives. Stats: Strength: 20, Health: 20, Wisdom: 20.
rogue_info = {"Weapons": ["Dagger", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20.}}
#Cleric Dictionary: Weapons: Mace, Warhammer, Morning Star. Stats: Strength: 10, Health: 30, Wisdom: 20.
cleric_info = {"Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20.}}
#Create Character Function
def create_character():
    #Display Class Options
    print("Welcome to the Character Creator!")
    print("Choose your class:")
    #1. Fighter, Display Fighter Stat Dictionary
    print(f"1. Fighter: {fighter_info['Stats']}")
    #2. Rogue, Display Rogue Stat Dictionary
    print(f"2. Rogue: {rogue_info['Stats']}")
    #3. Cleric, Display Cleric Stat Dictionary
    print(f"3. Cleric: {cleric_info['Stats']}")
    #Class is set to input type 1-3 to choose your class
    c_class = input("Enter the number of your class choice: ")
    #Check Class Function
    def check_class(c_class):
        #If Class is set to 1
        if c_class == "1":
            #Display Fighter Stats
            print(f"Fighter Stats: {fighter_info['Stats']}")
            #You have two empty stats
            print("You have two empty stats.")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Fighter Stats
            fighter_info['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Fighter Stats
            fighter_info['Stats']['Intelligence'] = intelligence
            #Display Fighter Stats
            print(f"Fighter Stats: {fighter_info['Stats']}")
            #Display Fighter List
            print(f"Choose your weapon: {fighter_info['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            #Add Weapon Choice to Fighter Info
            fighter_info['Stats']['Weapon'] = weapon_choice
            print(fighter_info)
            #Run Menu
        #If Class is set to 2
        if c_class == "2":
            #Display Rogue Stats
            print(f"Rogue Stats: {rogue_info['Stats']}")
            #You have 2 empty stats
            print("You have two empty stats.")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Rogue Stats
            rogue_info['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Rogue Stats
            rogue_info['Stats']['Intelligence'] = intelligence
            #Display Rogue Stats
            print(f"Rogue Stats: {rogue_info['Stats']}")
            #Display Rogue List
            print(f"Choose your weapon: {rogue_info['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            #Run Menu
        #If Class is set to 3
        if c_class == "3":
            #Display Cleric Stats
            print(f"Cleric Stats: {cleric_info['Stats']}")
            #You have 2 empty stats
            print("You have two empty stats.")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Cleric Stats
            cleric_info['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Cleric Stats
            cleric_info['Stats']['Intelligence'] = intelligence
            #Display Cleric Stats
            print(f"Cleric Stats: {cleric_info['Stats']}")
            #Display Cleric List
            print(f"Choose your weapon: {cleric_info['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            #Run Menu

    #Run Check Class Function
    check_class(c_class)
create_character()
