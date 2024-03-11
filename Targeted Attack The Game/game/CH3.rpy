image choice8:
    "videos/Choice Screens/CH3_INTRO.jpg"
    zoom 1.5

image choice9:
    "videos/Choice Screens/CH3_A0.jpg"
    zoom 1.5

image choice10:
    "videos/Choice Screens/CH3_B0.jpg"
    zoom 1.5

image choice11:
    "videos/Choice Screens/CH3_C0+ALT.jpg"
    zoom 1.5

label CH3:
    scene black
    $ renpy.movie_cutscene("videos/CH3/CH3_INTRO.webm", loops=0, stop_music=True)

    show choice8 at truecenter
    $ choice_screen_style = "choice_vbox_custom_right"
    menu:
        "Give them access to the app with limited functionality.":
            jump CH3_A0

        "Make the journalists wait till the launch of the app.":
            jump CH3_B0

        "Invite them to the test the app in a controlled environment.":
            jump CH3_C0

    label CH3_A0:
        scene black
        $ renpy.movie_cutscene("videos/CH3/CH3_A0.webm", loops=0, stop_music=True)

        show choice9 at truecenter
        $ choice_screen_style = "choice_vbox_custom_right"
        menu:
            "Invite them to the test the app in a controlled environment.":
                scene black
                $ renpy.movie_cutscene("videos/CH3/CH3_A1.webm", loops=0, stop_music=True)
                jump CH3_C0_ALT

            "Make the journalists wait till the launch of the app.":
                scene black
                $ renpy.movie_cutscene("videos/CH3/CH3_A2.webm", loops=0, stop_music=True)

        jump CH4

    label CH3_B0:
        scene black
        $ renpy.movie_cutscene("videos/CH3/CH3_B0.webm", loops=0, stop_music=True)

        show choice10 at truecenter
        $ choice_screen_style = "choice_vbox_custom_right4"
        menu:
            "Give them access to the app with limited functionality.":
                jump CH3_A0

            "Make the journalists wait till the launch of the app.":
                scene black
                $ renpy.movie_cutscene("videos/CH3/CH3_B1.webm", loops=0, stop_music=True)

            "Invite them to the test the app in a controlled environment.":
                jump CH3_C0

        jump CH4

    label CH3_C0:
        scene black
        $ renpy.movie_cutscene("videos/CH3/CH3_C0.webm", loops=0, stop_music=True)
        jump CH3_C0_Options

    label CH3_C0_ALT:
        scene black
        $ renpy.movie_cutscene("videos/CH3/CH3_C0_ALT.webm", loops=0, stop_music=True)
        jump CH3_C0_Options

    label CH3_C0_Options:
        show choice11 at truecenter
        $ choice_screen_style = "choice_vbox_custom_left"
        menu:
            "Tell the journalist that you will look further into the possibility.":
                scene black
                $ renpy.movie_cutscene("videos/CH3/CH3_C1.webm", loops=0, stop_music=True)

            "We are very sorry, but a high-security project, can not go outside the company.":
                scene black
                $ renpy.movie_cutscene("videos/CH3/CH3_C2.webm", loops=0, stop_music=True)

        jump CH4