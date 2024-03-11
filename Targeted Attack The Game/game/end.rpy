label credits:
    scene black
    $ renpy.movie_cutscene("videos/Credits/RIK1.webm", loops=0, stop_music=True)

    if segment:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK2_1.webm", loops=0, stop_music=True)
    elif twofactor:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK2_2.webm", loops=0, stop_music=True)
    elif activedirectory:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK2_3.webm", loops=0, stop_music=True)

    scene black
    $ renpy.movie_cutscene("videos/Credits/RIK3.webm", loops=0, stop_music=True)

    if datamovement:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK4_1.webm", loops=0, stop_music=True)
    elif forensic:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK4_2.webm", loops=0, stop_music=True)

    
    if shutdownserver:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK6_1.webm", loops=0, stop_music=True)
    elif sleep:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK6_2.webm", loops=0, stop_music=True)
    elif isolateserver:
        scene black
        $ renpy.movie_cutscene("videos/Credits/RIK6_3.webm", loops=0, stop_music=True)

    play music "audio/mamaimacriminal.mp3"
    show bad_ending at truecenter
    with irisin
    pause 2.0
    "Bad Ending"

    # This ends the game.
    return
    