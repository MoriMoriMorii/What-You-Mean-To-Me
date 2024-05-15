define switch = False
label demo_4m:  
    stop music
    "Les get this party startedd"
    phone call "n"
    phone_n "Yooo check it, I got Monika on the line and we're playing Russian Roulette"
    phone_m "We are {i}not{/i} doing tha-{nw}"
    play sound "sfx/gun.mp3"
    "A shot rings out"
    phone_n "Gotta go."
    phone end call
    "???"
    pause 1.0
    "This is kind of boring"
    phone discussion "dev_gc":
        "dev" "You can talk to me~"
        "dev" "You can talk to me"
        "dev" "You can talk to me-"
        "dev" "If you're lonely you can talk to me"
        "mc" "Hey bulldog - The Beatles"
    phone end discussion
    menu:
        "Add event?"
        "Yes":
            $ switch = True
        "No":
            $ switch = False
    if switch:
        init 100 python in phone.calendar:
            random_event = Calendar(4, 2023, THURSDAY)
            add_calendar_to_all_characters(random_event)
            random_event[20].description = "Blaze it."
    else:
        "L"
            
    call screen phone()
    return
