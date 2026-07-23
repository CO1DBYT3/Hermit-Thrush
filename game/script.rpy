## =============================================================================
##  HERMIT THRUSH
##  A short Ren'Py scene
##
##  Author's note (not shown in-game):
##    "the hermit thrush is relevant for time travel later" — kept here as a
##    reminder for future chapters; the bird's migration/lifespan is meant to
##    pay off later in the story.
##
##  Formatting key carried over from the draft:
##    "-" lines  -> internal thought (unspoken, italic, no name)
##    "="  lines -> spoken aloud (has a name box)
## =============================================================================

## -----------------------------------------------------------------------------
## CHARACTERS
## -----------------------------------------------------------------------------
define w = Character("Kazuki", who_color="#4b64d6")

# Thoughts get their own "voice": no name box, soft grey italics, slightly
# slower text speed than spoken lines so they read like an internal drift.
define thought = Character(
    None,
    what_prefix="{i}",
    what_suffix="{/i}",
    what_color="#9aa3ad",
    what_size=32,
)


## -----------------------------------------------------------------------------
## TRANSFORMS
## -----------------------------------------------------------------------------
transform drift_in:
    alpha 0 yoffset 12
    ease 0.8 alpha 1.0 yoffset 0

transform paper_float:
    ease 6.0 yoffset -6
    ease 6.0 yoffset 6
    repeat

transform toward_window:
    zoom 2
    xalign 0.5
    yalign 0.5
    ease 20.0 zoom 1.18 xalign 0.60 yalign 0.48

## A soft sepia veil used to mark the flashback as a memory rather than "now".
screen memory_tint():
    add Solid("#3b241a55")

## -----------------------------------------------------------------------------
## IMAGES  (placeholder art generated for you — swap these for real art
## whenever you like; just keep the same filenames or update the paths below)
## -----------------------------------------------------------------------------
image bg room present = Transform(
    "images/bg_room_present.png",
    fit="cover"
)
image bg room flashback = Transform(
    "images/bg_room_flashback.png",
    fit="cover"
)
image bg window night = Transform(
    "images/bg_window_night.png",
    fit="cover"
)
image paper = Transform(
    "images/paper_folded.png",
    fit="cover"
)

## -----------------------------------------------------------------------------
## AUDIO  (placeholder sounds generated for you — swap for real recordings
## whenever you like; a real hermit thrush call would elevate this a lot)
## -----------------------------------------------------------------------------
define audio.thrush_call = "audio/sfx_hermit_thrush.wav"
define audio.room_hum = "audio/amb_quiet_room.mp3"
define audio.wind = "audio/amb_wind.mp3"
define audio.clock = "audio/sfx_clock_tick.mp3"
init python:

    renpy.music.register_channel(
        "ambient",
        mixer="music",
        loop=True,
        tight=True,
    )

    renpy.music.register_channel(
        "nature",
        mixer="sfx",
        loop=True,
        tight=True,
    )


## -----------------------------------------------------------------------------
## LABEL: START
## -----------------------------------------------------------------------------
label start:
    play ambient audio.room_hum fadein 1 loop
    play music audio.clock volume 0.1 loop
    scene bg room present with dissolve
    pause 2.0

    thought "The air is stale..."
    thought "...as if there's something rotting in the vicinity."
    thought "How long has it been since I last cleaned my room?"

    play sound audio.thrush_call volume 3 fadein 1.0 loop

    thought "I hear the chorus of a hermit thrush outside my window."
    thought "It's close to winter now, so I guess this will be the last time I hear this creature."
    thought "For the last eight years, during the months of spring, he's been outside my window."
    thought "I wonder what I was doing that day. Those days are clouded in evanescence now."
    thought "I rushed back home from school. I was probably pathetic..."

    ## -------------------------------------------------------------------
    ## FLASHBACK — eight years ago
    ## -------------------------------------------------------------------
    show screen memory_tint
    scene bg room flashback with wipeleft
    stop ambient fadeout 1.0
    play ambient audio.wind fadein 1.5 loop

    w "The world hasn't been the best for the both of us."
    scene bg room flashback at toward_window with dissolve
    pause 1.0
    thought "8 years ago i found this hatchling injured in the leg."
    thought "i thought he was probably done for..."
    thought "but he's still here."

    hide screen memory_tint

    ## -------------------------------------------------------------------
    ## PRESENT
    ## -------------------------------------------------------------------
    scene bg room present with wiperight
    stop ambient fadeout 1.0
    stop sound fadeout 1.0
    play ambient audio.room_hum fadein 2.0 loop
    play music audio.clock loop fadein 2.0 volume 0.1 loop

    thought "A hermit thrush has a lifespan of around eight years. This is probably this guy's last winter."
    thought "He'll migrate south in a few weeks — probably right at the end of his life cycle."
    thought "Migrating probably makes his life a little less mundane than mine."

    show paper at truecenter with dissolve
    show paper at paper_float

    thought "Looking at the base of my door, I can see a folded piece of paper."
    thought "It was probably my parents... I get up from bed and go look at it."

    w "I turn twenty-five today, huh. A quarter of a century."

    hide paper with dissolve

    thought "It's a birthday card from my parents. They've stopped nagging me about going out, or getting a job, for seven months now."
    thought "I don't even have a college degree, and I barely passed high school. If I were to do something, it'd probably be some physical job."

    w "Apparently it's a Sunday today. My dad's probably home."

    thought "All the days of the week have mushed together for me by now. It doesn't matter if it's a Monday or a Sunday."
    thought "There's no change in how I'd spend my day either way."

    w "...I wonder if I should go down and talk with them."

    thought "..."

    ## -------------------------------------------------------------------
    ## CHOICE — a small branch so this plays like a scene, not just a
    ## monologue. Both paths are short; extend either into a full label
    ## once you write what happens next.
    ## -------------------------------------------------------------------
    menu:
        "Go downstairs and talk to them.":
            jump ending_talk

        "Stay in the room, like always.":
            jump ending_stay

## -----------------------------------------------------------------------------
## ENDINGS
## -----------------------------------------------------------------------------
label ending_talk:

    scene bg window night with dissolve
    stop ambient fadeout 2.0

    thought "For the first time in months, I open the door."
    thought "The card is still in my hand."

    w "...Happy birthday to me, I guess."

    return


label ending_stay:

    scene bg room present with dissolve

    thought "I fold the paper back up and set it on the desk."
    thought "Maybe next year."

    return
