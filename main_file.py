# Main Menu
# dictionary with options
# User has to choose a number to select an option
# Each option is associated with a number for easy selection
# What it would display
# 1. View Characters
# 2. Create Character
# 3. Edit Character
# 4. Exit
# menu_option is set to input type 1 to 4 to decide which option to choose

# Lizzie's File for Code

# VIEWING CHARACTER
# This will likely be a function: First check to see if they have one or more characters. If they do, show characters in a numbered list and have the user pick the number corresponding to the character they want to view. If user has no charcters, tell them and redirect to main menu where they can make a character.

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

# LV 1st RPG Pseudocode

# dictionary with the different options the player can choose
# Each option is associated with a number for easy selection
# The options include actions like "View", "Create", "Edit", and "Leave"

# CREATE CHARACTER FUNCTION
# This function allows the player to create a new character
# It prompts the player for character details and stores them in a dictionary
# User can choos a class "Rogue", "Cleric", "Fighter"

   # ROGUE CLASS
    # If user chooses 2 then it is Rouge
    # Needs 15 xp to level up and doubles from there
    # Stats
    # Strength: 20
    # Health: 20
    # Wisdom:20


   # Cleric CLASS
    # If user chooses 3 then it is Cleric
    # Needs 20 xp to level up and doubles from there
    # Stats
    # Strength: 10
    # Health: 30
    # Wisdom:20


# EDIT CHARACTER FUNCTION
# Running in the backround 
# This is a loop that allows the player to check if their character can level up
# If the character has enough XP, they level up
# When leveling up
# Cleric : add 1 to attack power, if cleric: add one spell slot if 
# new level is multiple of 5, tell user this charcter has leveled up
# Else return to the start(Check if character can level up)

# Level up loop
# def level_up_loop(character):
    # while true
       # xp_needed = character['level'] * 15 if character['class'] == 'Rogue' else character['level'] * 20
         # if character['xp'] >= xp_needed:
              # character['level'] += 1
              # character['xp'] -= xp_needed
              # character['attack_power'] += 1
              # if character['class'] == 'Cleric' and character['level'] % 5 == 0:
                # character['spell_slots'] += 1
              # print(f"{character['name']} has leveled up to level {character['level']}!")
        #  else:
                # break