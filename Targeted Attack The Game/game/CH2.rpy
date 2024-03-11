image choice5:
    "videos/Choice Screens/CH2_INTRO.jpg"
    zoom 1.5

image choice6:
    "videos/Choice Screens/CH2_A0B0C0.jpg"
    zoom 1.5

image choice7:
    "videos/Choice Screens/CH2_A1B1.jpg"
    zoom 1.5

default segment = False
default twofactor = False
default activedirectory = False

default breachdetection = False 

label CH2:
    scene black
    $ renpy.movie_cutscene("videos/CH2/CH2_INTRO.webm", loops=0, stop_music=True)

    show choice5 at truecenter
    $ choice_screen_style = "choice_vbox_custom_right3"
    menu:
        "Segment the network.\n[display_money_option(3)]" if check_money(3):
            $ spend_money(3)
            $ segment = True
            scene black
            $ renpy.movie_cutscene("videos/CH2/CH2_A0.webm", loops=0, stop_music=True)
            
        "Extend 2-factor authentication to 3rd parties.\n[display_money_option(2)]" if check_money(2):
            $ spend_money(2)
            $ twofactor = True
            scene black
            $ renpy.movie_cutscene("videos/CH2/CH2_B0.webm", loops=0, stop_music=True)

        "Use internal active directory to enforce strict access policies.":
            scene black
            $ activedirectory = True
            $ renpy.movie_cutscene("videos/CH2/CH2_C0.webm", loops=0, stop_music=True)

    show choice6 at truecenter
    $ choice_screen_style = "choice_vbox_custom_right"
    menu:
        "Ensure that we are fully compliant with all the regulatory requirements.":
            scene black
            $ renpy.movie_cutscene("videos/CH2/CH2_A1.webm", loops=0, stop_music=True)

        "Encrypt all the Intellectual Property.\n[display_money_option(2)]" if check_money(2):
            $ spend_money(2)
            scene black
            $ renpy.movie_cutscene("videos/CH2/CH2_B1.webm", loops=0, stop_music=True)

    show choice7 at truecenter
    $ choice_screen_style = "choice_vbox_custom_right"
    menu:
        "Invest in Breach Detection technology.\n[display_money_option(2)]" if check_money(2):
            $ spend_money(2)
            $ breachdetection = True
            scene black
            $ renpy.movie_cutscene("videos/CH2/CH2_A2.webm", loops=0, stop_music=True)

        "Carry out an audit of existing security technologies. Issue RFP documents to traditional security vendors.\n[display_money_option(2)]" if check_money(2):
            $ spend_money(2)
            scene black
            $ renpy.movie_cutscene("videos/CH2/CH2_B2.webm", loops=0, stop_music=True)

        "The Security Manager is responsible for control and monitoring with current tools.":
            scene black
            $ renpy.movie_cutscene("videos/CH2/CH2_C2.webm", loops=0, stop_music=True)

    jump CH3
