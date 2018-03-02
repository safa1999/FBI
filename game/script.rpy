# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character ("Amari")
define c = Character ("Coworker")




# The game starts here.

label start:
    $ coworkerPoint = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene shop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    "Well here I am."
    "Another boring day at work."

    show man

    c "YOOO WASSUP AMARI READY FOR ANOTHER DAY AT WORK?????"
    "That's my annoying coworker who always talks about the weirdest things. I mean, I don't hate him or anything but he's just..weird lmao."
    c "SO yesterday i discovered this thing called ASMR. Any idea what that stands for?"
    mc "HMMMM"

    menu:
        "Awesome Swag Must Re-use":
            jump idk1
        "Apple Sesame Mango Rice":
            $ coworkerPoint += 1    # if u pick choice, increase his points by 1
            jump idk2


    label idk1:
        c "How do you even come up with that."
        return
    label idk2:
        c "WHAT how does apple and mango go with rice?!" with vpunch


    c "Well anyways it stands for Autonomous Sensory Meridian Response."

    if coworkerPoint == 1:
        "You win i guess?"

    # This ends the game.

    return
