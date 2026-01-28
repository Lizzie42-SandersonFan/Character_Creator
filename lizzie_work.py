# Lizzie's File for Code
from trues_file import *
import time
import random

delay = 0.06

def type_print(string):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

# VIEWING CHARACTER
# This will likely be a function: First check to see if they have one or more characters. If they do, show characters in a numbered list and have the user pick the number corresponding to the character they want to view. If user has no charcters, tell them and redirect to main menu where they can make a character.
def view_character():
    global characters
    if not characters:
        type_print("You don't have any characters to view.\nRedirecting you to main menu to make a character\n")
        # Call main menu
    else:
        type_print("These are the characters you have to view\n")
        for character in characters:
            # Print the character names with a number before each one
            print(f"{character['Name']} ({character["Class"]})")
        print("Leave")
    
    # Get user to acctually select a chracter to view
    while True:
        view_choice = input("Type the name of the character you want to view (or 'Leave' if you want to go back to main menu):\n").strip()
        if view_choice == "Leave":
            type_print("Redirecting to main menu . . .")
            time.sleep(0.5)
            # Call main
            break
        for chara in characters:
            if view_choice == chara["Name"]:
                type_print(f"Viewing Character:\n Name: {chara['Name']}\n Class: {chara['Class']}\nStats:\n Strength: {chara['Stats']['Strength']}\n Health: {chara['Stats']['Health']}\n Wisdom: {chara['Stats']['Wisdom']}\n Dexterity: {chara['Stats']['Dexterity']}\n Intelligence: {chara['Stats']['Intelligence']}\n Weapon: {chara['Weapon']}\n")
                # For when it's added: Level: {chara['Stats']['Level']}\n XP: {chara['Stats']['XP']} <- added between Intelligence and weapon
                while True:
                    type_print("Would you like to\n1)View another character\nor\n2) Go back to main menu\n")
                    again = input("Type the number for the action you would like to do\n")
                    if again == "1":
                        view_character()
                        break
                    elif again == "2":
                        type_print("Redirecting to main menu . . .")
                        time.sleep(0.5)
                        break
                    else:
                        print("Invalid input. Try again")
                        continue
            else:
                print("Could not find the character you typed in. Check your spelling and punctuation.")
                continue

# When they have selected a character, show the character name, class, stats, current attack moves, XP amount, and level. Ask user if they would like to edit their character. If yes, direct to edit func. If no, redirect to main menu

# EDITING CHARACTER
# Delete a character, edit stats (including XP), edit attack menu.

# Deleting a character: Show user a numbered list of characters and have them select the number corresponding to the character they want to remove. Find that character (likely a dictionary with the character name as the dict name) and delete it.

# Edit stats: Ask user what they want to edit: add or remove XP, reroll a stat, edit attack menu/invintory

# Adding/removing XP: Ask if this is adding or removing. Have user type in a number and add or subtract based on previous answer

# Reroll a stat: Show the stats for the character and have the user type the name (as displayed) for the stat they want to reroll. Find that stat in the (likely) character dict and pick a number between 10 & 20. Show user the new stat and save it. Ask if they want to continue editing. Yes: Back to top of func. No: Redirect to main menu

# Edit Attack menu: Show user currect attack menu (It's a list). Ask if they want to add something or remove something
# Remove something: Show user numbered list of attacks and ask which number they would like to remove. Find that in the list and remove it from attack menu list. Add the same thing to a list of all POSSIBLE attacks the character could do (spells, aquired weapons, potions, etc.) When that is done, ask user if they want to conitue editing attack menu. If yes, back to top of attack menu edit. If no, redirect to main menu.
# Add something: Show user numbered list of POSSIBLE attacks character can do . Have user select number they would like to add to attack menu. If attack menu full (six moves), tell user and redirect to remove something. If there is room for another move, remove selected move from POSSIBLE moves and add it to Attack menu list. When that is done, ask user if they want to conitue editing attack menu. If yes, back to top of attack menu edit. If no, redirect to main menu.

def edit_character():
    def edit_XP():
        pass
        # Helper to add/remove. Have user type in number to add/remove. Update XP

    def edit_stat():
        pass
        # Have user select stat to reroll. Reroll with random number and save it

    def edit_invintory():
        pass
        # Use helper to know if adding or removing. Have user type in something to add\remove to invintory list

    def adding_removing():
        pass
        # Helper function that will ask the user if they are adding or removing

    global characters
    if not characters:
        type_print("You don't have any characters to edit.\nRedirecting you to main menu to make a character\n")
        # Call main menu
    else:
        type_print("These are the characters you have to edit\n")
        for character in characters:
            # Print the character names with a number before each one
            print(f"{character['Name']} ({character["Class"]})")
        print("Leave")

    # Get user to acctually select a character to view
    while True:
        view_choice = input("Type the name of the character you want to edit (or 'Leave' if you want to go back to main menu):\n").strip()
        if view_choice == "Leave":
            type_print("Redirecting to main menu . . .")
            time.sleep(0.5)
            # Call main
            break
        for chara in characters:
            if view_choice == chara["Name"]:
                pass 
                # Now give the user a list of things to edit and call the inner function corresponding to the selection
            else:
                print("Could not find the character you typed in. Check your spelling and punctuation.")
                continue

view_character()