# Lizzie's File for Code
from trues_file import *
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
    else:
        for i, characters in enumerate(characters):
            # Print the character names with a number before each one
            print(f"{i+1}: {characters['Class']}")
    
    # Get user to acctually select a chracter to view
    while True:
        view_choice = int(input("Type the number correxponding to that character you would like to view:\n"))
        if view_choice == i+1:
            print("User has choses to view character 1")
            print(f"{characters}")
            break
        else:
            print("It didn't work")

# When they have selected a character, show the character name, class, stats, current attack moves, XP amount, and level. Ask user if they would like to edit their character. If yes, direct to edit func. If no, redirect to main menu

# EDITING CHARACTER
# Delete a character, edit stats (including XP), edit attack menu.

# Deleting a character: Show user a numbered list of characters and have them select the number corresponding to the character they want to remove. Find that character (likely a dictionary with the character name as the dict name) and delete it.

# Edit stats: Ask user what they want to edit: add or remove XP, reroll a stat, edit attack menu

# Adding/removing XP: Ask if this is adding or removing. Have user type in a number and add or subtract based on previous answer

# Reroll a stat: Show the stats for the character and have the user type the name (as displayed) for the stat they want to reroll. Find that stat in the (likely) character dict and pick a number between 10 & 20. Show user the new stat and save it. Ask if they want to continue editing. Yes: Back to top of func. No: Redirect to main menu

# Edit Attack menu: Show user currect attack menu (It's a list). Ask if they want to add something or remove something
# Remove something: Show user numbered list of attacks and ask which number they would like to remove. Find that in the list and remove it from attack menu list. Add the same thing to a list of all POSSIBLE attacks the character could do (spells, aquired weapons, potions, etc.) When that is done, ask user if they want to conitue editing attack menu. If yes, back to top of attack menu edit. If no, redirect to main menu.
# Add something: Show user numbered list of POSSIBLE attacks character can do . Have user select number they would like to add to attack menu. If attack menu full (six moves), tell user and redirect to remove something. If there is room for another move, remove selected move from POSSIBLE moves and add it to Attack menu list. When that is done, ask user if they want to conitue editing attack menu. If yes, back to top of attack menu edit. If no, redirect to main menu.

view_character()