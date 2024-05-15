label act1:
    stop music fadeout 2.0
    scene black with dissolve
    $ af_enabled = True
    play music setstage
    show monika forward dist ce om at t11
    m "They say all's fair in love and war, but in the Literature Club, there's no telling where the line between the two blurs."
    m oe "Here, with each passing moment the tension tightens around you, like a noose around youur neck, forcing you to delve deeper into madness."
    m flus "In this world, writing is more than just a hobby, it's a means of survival."
    m dist ce  "Words are tools of power, and can be twisted into daggers or weaved into spells of manipulation and delusion."
    m flus oe "For as of now I have learned that not all stories have a happy ending."
    m dist "A satisfying ending."
    m ce "A {i}good{/i} ending."
    stop music fadeout 5.0
    scene black 
    with dissolve_scene_full
    pause 2.0
    scene bg bedroom_night
    with dissolve_scene_full
    play music late_lonely
    pause 1.0
    "Why are nights so long."
    "It's as if they span lifetimes."
    "I finally shut down my computer, glancing at the time."
    mc "1 am? God do I really have nothing better to do..."
    "I lay my head down on the pillow."
    mc "Not like much is happening tomorrow, except that weird thing with Nats and Sayo's weird book club."
    mc "Whatever, I'll worry about it in the morning."
    "I check my phone before I go to bed to look at my last text to Natsuki."
    phone discussion "nats":
        "n" "i bettr c u there dummy >:("
    phone end discussion
    "Oh right..."
    "Nats wants me to stop by, said earlier she had a surprise for me."
    "I ponder whatever that could be as I drift off to sleep."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg bedroom
    with dissolve_scene_half
    play music sunshine
    "Morning again."
    "Who'dve thunk it."
    "I slowly make my way out of bed and towards the kitchen for breakfast, not stopping to look at the time."
    "There's no way I could be late anyway."
    scene bg kitchen with wipeleft
    mc "What sounds good...eggs, bacon, cereal-"
    #TODO Add knock sound effect
    "Suddenly, I hear knocking."
    "I gently open the door as two girls rush inside."
    show sayori turned lup rup pani ce at t21
    show natsuki cross doub oe at t22
    s om "[player]! Where were you this morning?"
    show sayori cm
    n om "We're gonna be late if you don't hurry up, dummy!"
    show natsuki cm
    s om "We were texting you all morning!"
    show sayori cm
    show natsuki cm
    mc "Huh?"
    "I turn my phone on as the texts begin to populate."
    phone discussion "sayo":
        "s" "Heyyyy"
        "s" "[player]!!!"
        "s" "ur gonna b lateeee!!!"
    phone end discussion
    phone discussion "nats":
        "n" "hey dummy sayori was tryin to txt u"
        "n" "[player]!!!"
    phone end discussion
    "Ah geez"
    mc "Well, at least call me next time!"
    n om "We did."
    show natsuki cm
    mc "You..what.."
    
    phone call "s"
    "{i}Voicemail playing{/i}"
    phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_n "Where are you dummy? We're gonna be late! GET OVER HERE!!!"
    phone end call
    "{i}Was I that fast asleep???{/i}"
    n ce om "Well don't just stand there, go get ready!"
    show natsuki cm
    mc "R-right!"
    scene bg bedroom 
    with wipeleft
    "Oh man oh man oh man..."
    "I struggle to get ready quickly, and then go outside to meet the girls on the sidewalk"
    scene bg residential_day
    show sayori turned happ at t21
    show natsuki cross angr  at t22
    n om "What took you so long?"
    show natsuki cm
    mc "I was in there for 5 minutes!"
    n ce om "5 minutes too long, now lets go!"
    show natsuki cm
    window hide
    pause 1.0
    $ af_enabled = False
    show natsuki cross fta at t22
    show natsuki at lhide
    hide natsuki
    window show
    s pani ce om "Wait up!!!"
    window hide
    pause 1.0
    show sayori at rhide
    hide sayori
    $ af_enabled = False
    window show
    "They ran off without me!"
    mc "Hold on!!!"
    "I catch up to Sayori, Natsuki running off with a tray of god knows what."
    show sayori turned pani ce om at l11
    mc "Gotcha!"
    s "Uwaaa!"
    show sayori happ ce cm at t11
    s om "You got me~"
    show sayori cm oe
    mc "What's got you guys in such a rush? It's 30 minutes 'til school starts anyway..."
    return