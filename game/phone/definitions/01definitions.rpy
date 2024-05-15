# /!\ default
# pc as in phone character :monikk:
default pc_sayori  = phone.character.Character("Sayori", phone.config.basedir + "sayori_icon.png", "s", 21, "#22Abf8")
default pc_mc      = phone.character.Character("[player]", phone.config.basedir + "mc_icon.png", "mc", 35, "#000000")
default pc_yuri    = phone.character.Character("Yuri", phone.config.basedir + "yuri_icon.png", "y", 20, "#a327d6")
default pc_monika  = phone.character.Character("Monika", phone.config.basedir + "monika_icon.png", "m", 40, "#0a0")
default pc_natsuki = phone.character.Character("Natsuki", phone.config.basedir + "natsuki_icon.png", "n", 45, "#fbb")
default pc_lily = phone.character.Character("Lily", phone.config.basedir + "default_icon.png", "l", 45, "#9179b1")

default pov_key = "mc"

define phone_s  = Character("Sayori", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_mc = Character("[player]", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_y  = Character("Yuri", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_n  = Character("Natsuki", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_m  = Character("Monika", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_l  = Character("Lily", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python in phone.calendar:
    june_2023_calendar = Calendar(6, 2023, MONDAY)
    add_calendar_to_all_characters(june_2023_calendar)
    june_2023_calendar[30].description = "Woah."

init phone register:
    define "Lit Club GC":
        add "s" add "mc" add "y" add "m" add "n"
        icon phone.config.basedir + "default_icon.png"
        as lit_club key "lc"
init phone register:
    define "Sayori":
        add "s" add "mc"
        icon phone.config.basedir + "sayori_icon.png"
        as sayo key "sayo"
init phone register:
    define "Natsuki":
        add "n" add "mc"
        icon phone.config.basedir + "natsuki_icon.png"
        as nats key "nats"
label phone_discussion_test:
    phone discussion "lc":
        label "'Sayori' has been added to the group"
        label "'[player]' has been added to the group"
        label "'Yuri' has been added to the group"
        label "'Monika' has been added to the group"
        label "'Natsuki' has been added to the group"
        "m" "Okay everyone! Welcome to the Literature club group chat!"
        "n" "monika we're in a texting chat no need 4 punctuation"
        "y" "But that would not be polite, Natsuki"
        "n" "arghhh"
    phone end discussion

    return

label phone_call_test:
    phone call "s"
    phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_mc "Hey!"
    "Why is she always this energetic?"
    phone end call
    "..."

    return