image choice15:
    "videos/Choice Screens/CH5_INTRO.jpg"
    zoom 1.5

image choice16:
    "videos/Choice Screens/CH5_A0.jpg"
    zoom 1.5

default shutdownserver = False
default sleep = False
default isolateserver = False

label CH5:
    if checklogs:
        jump CH5_ALT

    scene black
    $ renpy.movie_cutscene("videos/CH5/CH5_INTRO.webm", loops=0, stop_music=True)
    
    show choice15 at truecenter
    $ choice_screen_style = "choice_vbox_custom_left2"
    menu:
        "Shut the servers down! We can’t afford any more data to leak out of the company!":
            $ shutdownserver = True
            scene black
            $ renpy.movie_cutscene("videos/CH5/CH5_A0.webm", loops=0, stop_music=True)

            show choice16 at truecenter
            $ choice_screen_style = "choice_vbox_custom_right"
            menu:
                "Call IT to not shut the servers down, just isolate them.":
                    scene black
                    $ renpy.movie_cutscene("videos/CH5/CH5_A1.webm", loops=0, stop_music=True)

                "I will make sure those servers get shut down!":
                    scene black
                    $ renpy.movie_cutscene("videos/CH5/CH5_A2.webm", loops=0, stop_music=True)

        "Pull out the network cables and call the police!":
            $ isolateserver = True
            scene black
            $ renpy.movie_cutscene("videos/CH5/CH5_B0.webm", loops=0, stop_music=True)

        "It’s probably just another bluff - Don’t worry about it.":
            $ sleep = True
            scene black
            $ renpy.movie_cutscene("videos/CH5/CH5_C0.webm", loops=0, stop_music=True)

    jump credits

label CH5_ALT:
    scene black
    $ renpy.movie_cutscene("videos/CH5/CH5_ALT.webm", loops=0, stop_music=True)

    play music "audio/lethergo.mp3"
    show good_ending
    with zoomin
    pause 2.0
    "Good Ending"

    # This ends the game.
    return
