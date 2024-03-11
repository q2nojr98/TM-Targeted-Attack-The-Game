# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Dave")
define j = Character("Julian")
define m = Character("Melinda")
define r = Character("Randall")
define v = Character("Venessa")
define p = Character("Vic")

# Define images
# Character images
image Dave:
    "dave.jpg"
    zoom 2

image Julian:
    "julian.jpg"
    zoom 2

image Melinda:
    "melinda.jpg"
    zoom 2

image Randall:
    "randall.jpg"
    zoom 2

image Venessa:
    "vanessa.jpg"
    zoom 2

image Vic:
    "vic.jpg"
    zoom 2

image Fugle:
    "top.jpg"
    zoom 2

# TM Logo
image TM:
    "by-trendmicro"

# Money Image
image ball:
    "TM_TBall.png"
    zoom 0.05

# Define a screen to display the current amount of money
screen money_display_screen():
    hbox:
        xalign 0.10  # Align the hbox to the left
        yalign 0.18  # Align the hbox to the top

        for i in range(money):
            add "TM_TBall.png" xzoom 0.075 yzoom 0.075

init python:
    # Function to display the cost of choice in images
    def display_money_option(cost):
        return "{" + "}{".join(["image=ball" for _ in range(cost)]) + "}"
    
    # Function to check if enough money is available
    def check_money(cost):
        global money
        if money >= cost:
            return True
        else:
            return False

    # Function to handle spending money
    def spend_money(cost):
        global money
        money -= cost

# Initialize the money variable
default money = 6

# default choice screen style
default choice_screen_style = "choice_vbox_custom_right"

# The game starts here.
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # scene bg room
    scene black

    show Dave at truecenter
    "You will be playing as Dave, the Chief Information Officer (CIO) of The Fugle"
    d "Hello my name is Dave, CIO of The Fugle"
    d "An experienced manager and a true visionary. He is the heart and the mind behind the app. His amazing programming background and leadership skills help guide our company to a better future."
    hide Dave

    show Randall at truecenter
    with dissolve
    r "Hi I'm Randall the Security Manager"
    r "Your right-hand man. He takes care of our corporate security and our customers’ privacy. Randall manages a dream team of professionals, keeping customer data safe at The Fugle."
    hide Randall

    show Melinda at truecenter
    with dissolve
    m "CEO of The Fugle"
    m "Melinda develops and drives the entire corporate strategy. One of the most visionary CEOs in the industry and the very best when it comes to turning ideas into reality."
    hide Melinda

    show Venessa at truecenter
    with dissolve
    v  "I'm Venessa the Marketing Director."
    v "MBA in Marketing and Communications from Yarvard University; professionalism personified. Vanessa knows all about marketing in the InfoSec sector and beyond. She is the inspiration and leader behind every Fugle marketing campaign."
    hide Venessa

    show Julian at truecenter
    with dissolve
    j "Call me Julian, PR Manager"
    j "The one and only, Julian has been in the industry for more than a decade and was last year awarded “Best PR Manager” by the Journalists’ Review. Reporting to Vanessa, he is always friendly, always professional, always ready to help the media do their job."
    hide Julian

    show Vic at truecenter
    with dissolve
    p "I am with the Police, Seargant Vic Harrisson"
    p "Seargant Harrisson does not trust new technologies, still believing in traditional investigation methods; a very thorough detective who will go on make a great career in the Police Department. If you want to see how his career progresses, check www.2020.trendmicro.com."
    hide Vic

    show Fugle at truecenter
    with dissolve
    "You are the CIO of a global organization called The Fugle, on the verge of making the first release of a biometrically authenticated mobile payment app."
    "You will steer the project through its final stages, dealing with your internal security team, your colleagues in Marketing and PR and of course your CEO."
    "There are many competitors and individuals out there who would love to get their hands on the data held by your organization at such a critical time."
    "Can you make the right choices?"
    "Can you keep the project on time and on budget?"
    "Can you protect your company from attack?"
    hide Fugle

    jump CH1