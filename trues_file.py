#TE 2nd Character Creator
#True's Part of the Character Creator
#Import Random
import random
import sys
import time

def slow_print(text, delay=0.1):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()  # Force the character to appear immediately
        time.sleep(delay)
    print()  # Print a final newline character

#Fighter Dictionary: Weapons: Greatsword, Greataxe, Maul. Stats: Strength: 30, Health: 20, Wisdom: 10.
fighter = {"Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10.}}
#Rogue Dictionary: Weapons: Dagger, Blowgun, Knives. Stats: Strength: 20, Health: 20, Wisdom: 20.
rogue = {"Weapons": ["Daggers", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20.}}
#Cleric Dictionary: Weapons: Mace, Warhammer, Morning Star. Stats: Strength: 10, Health: 30, Wisdom: 20.
cleric = {"Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20.}}
#List for Characters
characters = []
#Create Character Function
def create_character():
    #Display Class Options
    slow_print("Welcome to the Character Creator!")
    print("Choose your class:")
    #1. Fighter, Display Fighter Stat Dictionary
    print(f"1. Fighter: {fighter['Stats']}")
    #2. Rogue, Display Rogue Stat Dictionary
    print(f"2. Rogue: {rogue['Stats']}")
    #3. Cleric, Display Cleric Stat Dictionary
    print(f"3. Cleric: {cleric['Stats']}")
    #Class is set to input type 1-3 to choose your class
    c_class = input("Enter the number of your class choice: ")
    #Check Class Function
    def check_class(c_class):
        #If Class is set to 1
        if c_class == "1":
            #Display Fighter Stats
            print(f"Fighter Stats: {fighter['Stats']}")
            #You have two empty stats
            slow_print("You have two empty stats.")
            print("Rolling for your stats...")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            slow_print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Fighter Stats
            fighter['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            slow_print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Fighter Stats
            fighter['Stats']['Intelligence'] = intelligence
            #Display Fighter Stats
            print(f"Fighter Stats: {fighter['Stats']}")
            #Display Fighter List
            print(f"Choose your weapon: {fighter['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            #Add Weapon Choice to Fighter Info
            fighter['Stats']['Weapon'] = weapon_choice
            slow_print("Your finished stats:")
            print(f"Strength: {fighter['Stats']['Strength']}")
            print(f"Health: {fighter['Stats']['Health']}")
            print(f"Wisdom: { fighter['Stats']['Wisdom']}")
            print(f"Dexterity: {fighter['Stats']['Dexterity']}")
            print(f"Intelligence: {fighter['Stats']['Intelligence']}")
            print(f"Weapon: {fighter['Stats']['Weapon']}")
            slow_print("Character creation complete!")
            #Run Menu
        #If Class is set to 2
        if c_class == "2":
            #Display Rogue Stats
            slow_print(f"Rogue Stats: {rogue['Stats']}")
            #You have 2 empty stats
            slow_print("You have two empty stats.")
            print("Rolling for your stats...")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            slow_print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Rogue Stats
            rogue['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            slow_print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Rogue Stats
            rogue['Stats']['Intelligence'] = intelligence
            #Display Rogue Stats
            print(f"Rogue Stats: {rogue['Stats']}")
            #Display Rogue List
            print(f"Choose your weapon: {rogue['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            rogue['Stats']['Weapon'] = weapon_choice
            slow_print("Your finished stats:")
            print(f"Strength: {rogue['Stats']['Strength']}")
            print(f"Health: {rogue['Stats']['Health']}")
            print(f"Wisdom: {rogue['Stats']['Wisdom']}")
            print(f"Dexterity: {rogue['Stats']['Dexterity']}")
            print(f"Intelligence: {rogue['Stats']['Intelligence']}")
            print(f"Weapon: {rogue['Stats']['Weapon']}")
            slow_print("Character creation complete!")
            #Run Menu
        #If Class is set to 3
        if c_class == "3":
            #Display Cleric Stats
            slow_print(f"Cleric Stats: {cleric['Stats']}")
            #You have 2 empty stats
            slow_print("You have two empty stats.")
            print("Rolling for your stats...")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            slow_print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Cleric Stats
            cleric['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            slow_print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Cleric Stats
            cleric['Stats']['Intelligence'] = intelligence
            #Display Cleric Stats
            print(f"Cleric Stats: {cleric['Stats']}")
            #Display Cleric List
            print(f"Choose your weapon: {cleric['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            cleric['Stats']['Weapon'] = weapon_choice
            slow_print("Your finished stats:")
            print(f"Strength: {cleric['Stats']['Strength']}")
            print(f"Health: {cleric['Stats']['Health']}")
            print(f"Wisdom: {cleric['Stats']['Wisdom']}")
            print(f"Dexterity: {cleric['Stats']['Dexterity']}")
            print(f"Intelligence: {cleric['Stats']['Intelligence']}")
            print(f"Weapon: {cleric['Stats']['Weapon']}")
            slow_print("Character creation complete!")
            #Run Menu

    #Run Check Class Function
    check_class(c_class)
create_character()
