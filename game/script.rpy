# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Whomst")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lol 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show man

    # These display lines of dialogue.

    m "Wake me up inside."

    m "Wake me up and SAVE me from the nothign ive become."
    
    m "is your name linda?"
    
    menu:
        "Yes":
            jump correctAns
            
        "No":
            jump wrongAns
            
    label correctAns:
        m "I see youre a man of culture as well."
        return 
    label wrongAns:
        m "you fool. you absolute buffoon." 
        return 
    # This ends the game.

    return
