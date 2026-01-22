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

#True's Part of the Character Creator
#Import Random
#Create Character Function
    #Display Class Options
    #1. Fighter, Base Stats: Strength: 30, Health: 20, Wisdom: 10.
    #2. Rogue, Base Stats: Strength: 20, Health: 20, Wisdom: 20.
    #3. Cleric, Base Stats: Strength: 10, Health: 30, Wisdom: 20.

    #Class is set to input type 1-3 to choose your class.

    #If Class is set to 1
        #Fighter Base Stats is set to Strength: 30, Health: 20, Wisdom: 10.
        #Display You chose Fighter, your base stats are Fighter Base Stats

    #You have 2 empty stats
    #Roll for Dexterity
    #Dexterity is set a random number between 10 & 30
    #Display Your Dexterity is Dexterity

    #Roll for Intelligence
    #Intelligence is set a random number between 10 & 30
    #Display Your Intelligence is Intelligence

    #If Class is set to 1
        #Your fighter stats are Fighter Base Stats Dexterity: Dexterity, Intelligence: Intelligence
        #Display it is now time to choose your weapon.
        #Display Weapon Options
        #1. Greatsword
        #2. Maul
        #3. Greataxe
        #Weapon Options is set to input type 1-3 to choose your weapon.
        #If Weapon Options is set to 1
            #Display You chose Greatsword
            #You have finished creating your character!
            #You can now view your character.
            #Run Menu

    #If Weapon Options is set to 2
        #Display You chose Maul
        #You have finished creating your character!
        #You can now view your character.
        #Run Menu

    #If Weapon Options is set to 3
        #Display You chose Greataxe
        #You have finished creating your character!
        #You can now view your character.
        #Run Menu
    #If Class is set to 2
        #Your Cleric stats are Cleric Base Stats Dexterity: Dexterity, Intelligence: Intelligence
        #Display it is now time to choose your weapon.
        #Display Weapon Options
        #1. Daggers
        #2. Sword
        #3. Blowgun
        #Weapon Options is set to input type 1-3 to choose your weapon.
        #If Weapon Options is set to 1
            #Display You chose Daggers
            #You have finished creating your character!
            #You can now view your character.
            #Run Menu
        #If Weapon Options is set to 2
            #Display You chose Sword
            #You have finished creating your character!
            #You can now view your character.
            #Run Menu
        #If Weapon Options is set to 3
            #Display You chose Blowgun
            #You have finished creating your character!
            #You can now view your character.
            #Run Menu
    #If Class is set to 3
        #Your Rogue stats are Rogue Base Stats Dexterity: Dexterity, Intelligence: Intelligence
        #Display it is now time to choose your weapon.
        #Display Weapon Options
        #1. Mace
        #2. Warhammer
        #3. Morning Star
        #Weapon Options is set to input type 1-3 to choose your weapon.
        #If Weapon Options is set to 1
            #Display You chose Mace.
            #You have finished creating your character!
            #You can now view your character.
            #Run Menu
        #If Weapon Options is set to 2
            #Display You chose Warhammer.
            #You have finished creating your character!
            #You can now view your character.
            #Run Menu
        #If Weapon Options is set to 3
            #Display You chose Morning Star.
            #You have finished creating your character!
            #You can now view your character.
            #Run Menu
