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

#List for character weapons
#Fighter Dictionary: Weapons: Greatsword, Greataxe, Maul. Stats: Strength: 30, Health: 20, Wisdom: 10.
fighter_info = {"Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10.}}
#Rogue Dictionary: Weapons: Dagger, Blowgun, Knives. Stats: Strength: 20, Health: 20, Wisdom: 20.
rogue_info = {"Weapons": ["Daggers", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20.}}
#Cleric Dictionary: Weapons: Mace, Warhammer, Morning Star. Stats: Strength: 10, Health: 30, Wisdom: 20.
cleric_info = {"Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20.}}
#Create Character Function
def create_character():
    #Display Class Options
    slow_print("Welcome to the Character Creator!")
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
            slow_print("You have two empty stats.")
            print("Rolling for your stats...")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            slow_print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Fighter Stats
            fighter_info['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            slow_print(f"Your Intelligence is {intelligence}.")
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
            slow_print("Your finished stats:")
            print(f"Strength: {fighter_info['Stats']['Strength']}")
            print(f"Health: {fighter_info['Stats']['Health']}")
            print(f"Wisdom: { fighter_info['Stats']['Wisdom']}")
            print(f"Dexterity: {fighter_info['Stats']['Dexterity']}")
            print(f"Intelligence: {fighter_info['Stats']['Intelligence']}")
            print(f"Weapon: {fighter_info['Stats']['Weapon']}")
            slow_print("Character creation complete!")
            #Run Menu
        #If Class is set to 2
        if c_class == "2":
            #Display Rogue Stats
            slow_print(f"Rogue Stats: {rogue_info['Stats']}")
            #You have 2 empty stats
            slow_print("You have two empty stats.")
            print("Rolling for your stats...")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            slow_print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Rogue Stats
            rogue_info['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            slow_print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Rogue Stats
            rogue_info['Stats']['Intelligence'] = intelligence
            #Display Rogue Stats
            print(f"Rogue Stats: {rogue_info['Stats']}")
            #Display Rogue List
            print(f"Choose your weapon: {rogue_info['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            rogue_info['Stats']['Weapon'] = weapon_choice
            slow_print("Your finished stats:")
            print(f"Strength: {rogue_info['Stats']['Strength']}")
            print(f"Health: {rogue_info['Stats']['Health']}")
            print(f"Wisdom: {rogue_info['Stats']['Wisdom']}")
            print(f"Dexterity: {rogue_info['Stats']['Dexterity']}")
            print(f"Intelligence: {rogue_info['Stats']['Intelligence']}")
            print(f"Weapon: {rogue_info['Stats']['Weapon']}")
            slow_print("Character creation complete!")
            #Run Menu
        #If Class is set to 3
        if c_class == "3":
            #Display Cleric Stats
            slow_print(f"Cleric Stats: {cleric_info['Stats']}")
            #You have 2 empty stats
            slow_print("You have two empty stats.")
            print("Rolling for your stats...")
            #Roll for Dexterity
            dexterity = random.randint(10, 30)
            #Display Your Dexterity is Dexterity
            slow_print(f"Your Dexterity is {dexterity}.")
            #Add Dexterity to Cleric Stats
            cleric_info['Stats']['Dexterity'] = dexterity
            #Roll for Intelligence
            intelligence = random.randint(10, 30)
            #Display Your Intelligence is Intelligence
            slow_print(f"Your Intelligence is {intelligence}.")
            #Add Intelligence to Cleric Stats
            cleric_info['Stats']['Intelligence'] = intelligence
            #Display Cleric Stats
            print(f"Cleric Stats: {cleric_info['Stats']}")
            #Display Cleric List
            print(f"Choose your weapon: {cleric_info['Weapons']}")
            #Input Weapon Choice, Type the weapon you want
            weapon_choice = input("Type the weapon you want: ")
            cleric_info['Stats']['Weapon'] = weapon_choice
            slow_print("Your finished stats:")
            print(f"Strength: {cleric_info['Stats']['Strength']}")
            print(f"Health: {cleric_info['Stats']['Health']}")
            print(f"Wisdom: {cleric_info['Stats']['Wisdom']}")
            print(f"Dexterity: {cleric_info['Stats']['Dexterity']}")
            print(f"Intelligence: {cleric_info['Stats']['Intelligence']}")
            print(f"Weapon: {cleric_info['Stats']['Weapon']}")
            slow_print("Character creation complete!")
            #Run Menu

    #Run Check Class Function
    check_class(c_class)
create_character()
