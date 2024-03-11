image choice12:
    "videos/Choice Screens/CH4_INTRO_W.jpg"
    zoom 1.5

image choice13:
    "videos/Choice Screens/CH4_INTRO.jpg"
    zoom 1.5

image choice14:
    "videos/Choice Screens/CH4_B0.jpg"
    zoom 1.5

default datamovement = False
default forensic = False

default checklogs = False

label CH4:
    if breachdetection:
        scene black
        $ renpy.movie_cutscene("videos/CH4/CH4_INTRO_W.webm", loops=0, stop_music=True)
    else:
        scene black
        $ renpy.movie_cutscene("videos/CH4/CH4_INTRO.webm", loops=0, stop_music=True)

    $ config.menu_include_disabled = False
    label CH4_Options:

        if breachdetection:
            show choice12 at truecenter
            $ choice_screen_style = "choice_vbox_custom_left"
        else:
            show choice13 at truecenter
            $ choice_screen_style = "choice_vbox_custom_left2"
        menu:
            "Don’t change the schedule, but run a data movement check.":
                scene black
                $ renpy.movie_cutscene("videos/CH4/CH4_A0.webm", loops=0, stop_music=True)

            "Engage an external Forensic Investigation.":
                jump CH4_B0

            "Have the Security team check the Breach Detection System logs." if breachdetection:
                $ checklogs = True
                scene black
                $ renpy.movie_cutscene("videos/CH4/CH4W_C0.webm", loops=0, stop_music=True)

    jump CH5

    label CH4_B0:
        scene black
        $ renpy.movie_cutscene("videos/CH4/CH4_B0.webm", loops=0, stop_music=True)

        show choice14 at truecenter
        $ choice_screen_style = "choice_vbox_custom_left"
        menu:
            "Keep the project on schedule no matter what let the PR department deal with it.":
                scene black
                $ renpy.movie_cutscene("videos/CH4/CH4_B1.webm", loops=0, stop_music=True)

            "Keep the project running, engage external forensics, don’t delay the app launch.":
                scene black
                $ renpy.movie_cutscene("videos/CH4/CH4_B2.webm", loops=0, stop_music=True)

    jump CH5
