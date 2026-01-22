# LV 1st RPG Pseudocode

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