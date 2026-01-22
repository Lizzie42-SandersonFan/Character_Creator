#TE 2nd Character Creator
#True's Part of the Character Creator
#Import Random
import random

#List for character weapons
#Fighter Dictionary: Weapons: Greatsword, Greataxe, Maul. Stats: Strength: 30, Health: 20, Wisdom: 10.
fighter_info = {"Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}}
#Rogue Dictionary: Weapons: Dagger, Blowgun, Knives. Stats: Strength: 20, Health: 20, Wisdom: 20.
rogue_info = {"Weapons": ["Dagger", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}}
#Cleric Dictionary: Weapons: Mace, Warhammer, Morning Star. Stats: Strength: 10, Health: 30, Wisdom: 20.
cleric_info = {"Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}}
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
            #Run Menu
        #If Class is set to 2
            #Display Rogue Stats
            #You have 2 empty stats
            #Roll for Dexterity
            #Dexterity is set a random number between 10 & 30
            #Display Your Dexterity is Dexterity
            #Add Dexterity to Rogue Stats
            #Roll for Intelligence
            #Intelligence is set a random number between 10 & 30
            #Display Your Intelligence is Intelligence
            #Add Intelligence to Rogue Stats
            #Display Rogue Stats
            #Display Rogue List
            #Input Weapon Choice, Type the weapon you want
            #Run Menu
        #If Class is set to 3
            #Display Cleric Stats
            #You have 2 empty stats
            #Roll for Dexterity
            #Dexterity is set a random number between 10 & 30
            #Display Your Dexterity is Dexterity
            #Add Dexterity to Cleric Stats
            #Roll for Intelligence
            #Intelligence is set a random number between 10 & 30
            #Display Your Intelligence is Intelligence
            #Add Intelligence to Cleric Stats
            #Display Cleric Stats
            #Display Cleric List
            #Input Weapon Choice, Type the weapon you want
            #Run Menu

    #Run Check Class Function
