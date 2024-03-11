define config.menu_include_disabled = True

image choice1:
    "videos/Choice Screens/CH1_INTRO.jpg"
    zoom 1.5

image choice2:
    "videos/Choice Screens/CH1_A0+ALT.jpg"
    zoom 1.5

image choice3:
    "videos/Choice Screens/CH1_B0.jpg"
    zoom 1.5

image choice4:
    "videos/Choice Screens/CH1_C0.jpg"
    zoom 1.5

label CH1:
    scene black
    $ renpy.movie_cutscene("videos/CH1/CH1_INTRO.webm", loops=0, stop_music=True)
    
    show choice1 at truecenter
    $ choice_screen_style = "choice_vbox_custom_right"
    show screen money_display_screen()
    menu:
        "Outsource to a third party to help us identify any security issues (the ones related to the app).":
            jump CH1_A0

        "Postpone the launch of the app and work on it internally.":
            jump CH1_B0

        "Release on schedule and address any vulnerabilities with updates.":
            jump CH1_C0

    label CH1_A0:
        scene black
        $ renpy.movie_cutscene("videos/CH1/CH1_A0.webm", loops=0, stop_music=True)

        show choice2 at truecenter
        $ choice_screen_style = "choice_vbox_custom_right"
        menu:
            "The one that has been working with us, but never on this level.\n[display_money_option(1)]" if check_money(1):
                $ spend_money(1)
                jump CH1_A1
                label  CH1_A1:
                    $ renpy.movie_cutscene("videos/CH1/CH1_A1.webm", loops=0, stop_music=True)

            "TECHSPEC, highly recommended by the market, fully professional team of great  programmers, but very expensive.\n[display_money_option(3)]" if check_money(3):
                $ spend_money(3)
                jump CH1_A2
                label  CH1_A2:
                    $ renpy.movie_cutscene("videos/CH1/CH1_A2.webm", loops=0, stop_music=True)

            "ITFr33X, recommended by one of the IT team members - a group of talented freelancers, who will do it fast and for a reasonable price.\n[display_money_option(2)]" if check_money(2):
                $ spend_money(2)
                jump CH1_A3
                label  CH1_A3:
                    $ renpy.movie_cutscene("videos/CH1/CH1_A3.webm", loops=0, stop_music=True)

        jump CH2
        
    label CH1_B0:
        scene black
        $ renpy.movie_cutscene("videos/CH1/CH1_B0.webm", loops=0, stop_music=True)

        show choice3 at truecenter
        $ choice_screen_style = "choice_vbox_custom_right"
        menu:
            "Outsource to a third party to help us identify any security issues.":
                jump CH1_B1
                label  CH1_B1:
                    $ renpy.movie_cutscene("videos/CH1/CH1_B1.webm", loops=0, stop_music=True)
                    jump CH1_A0_ALT

            "Invest in some vulnerability scanning tools and training for the team.\n[display_money_option(2)]" if check_money(2):
                $ spend_money(2)
                jump CH1_B2
                label  CH1_B2:
                    $ renpy.movie_cutscene("videos/CH1/CH1_B2.webm", loops=0, stop_music=True)

            "Work on any vulnerabilities after the first release of the app.":
                jump CH1_B3
                label  CH1_B3:
                    $ renpy.movie_cutscene("videos/CH1/CH1_B3.webm", loops=0, stop_music=True)

        jump CH2

    label CH1_C0:
        scene black
        $ renpy.movie_cutscene("videos/CH1/CH1_C0.webm", loops=0, stop_music=True)
        
        show choice4 at truecenter
        $ choice_screen_style = "choice_vbox_custom_right2"
        menu:
            "Outsource to a third party to help us identify any security issues.":
                jump CH1_C1
                label  CH1_C1:
                    $ renpy.movie_cutscene("videos/CH1/CH1_C1.webm", loops=0, stop_music=True)
                    jump CH1_A0_ALT

            "Invest in some vulnerability scanning tools and training for the team.\n[display_money_option(2)]" if check_money(2):
                $ spend_money(2)
                jump CH1_C2
                label  CH1_C2:
                    $ renpy.movie_cutscene("videos/CH1/CH1_C2.webm", loops=0, stop_music=True)

            "Peer review of code using our own in-house developers.":
                jump CH1_C3
                label  CH1_C3:
                    $ renpy.movie_cutscene("videos/CH1/CH1_C3.webm", loops=0, stop_music=True)
        
        jump CH2

    label CH1_A0_ALT:
        scene black
        $ renpy.movie_cutscene("videos/CH1/CH1_A0_ALT.webm", loops=0, stop_music=True)

        show choice2 at truecenter
        $ choice_screen_style = "choice_vbox_custom_right"
        menu:
            "The one that has been working with us, but never on this level.\n[display_money_option(1)]" if check_money(1):
                $ spend_money(1)
                jump CH1_A1

            "TECHSPEC, highly recommended by the market, fully professional team of great  programmers, but very expensive.\n[display_money_option(3)]" if check_money(3):
                $ spend_money(3)
                jump CH1_A2

            "ITFr33X, recommended by one of the IT team members - a group of talented freelancers, who will do it fast and for a reasonable price.\n[display_money_option(2)]" if check_money(2):
                $ spend_money(2)
                jump CH1_A3

        jump CH2