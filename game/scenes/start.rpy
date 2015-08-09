init python:
    # Track things that happened in a sex scene
    
    # SexChoiceSets are backed by the Ren'Py store on top of StoreBackedSet,
    # and automatically define boolean accessors for the given *arguments
    # to modify the contents of the set.
    #
    # This is easier to track than thousands of separate variables, and less
    # error prone than using StoreBackedSet directly.
    akki_sex_choices = SexChoiceSet('akki_sex_choices', [
        'kissing',
        'breasts',
        'pectouch',
        'top_off',
        'below_waist',
        'thighs',
        'between_thighs',
        'naked_below',
        'mutual_touching',
        'missionary'
    ])
    kael_sex_choices = SexChoiceSet('kael_sex_choices', [
        'condom',
        'kissing',
        'foreplay',
        'before_pillow',
        'top_first',
        'undressing',
        'undressing_scene_top',
        'claire_top',
        'switched_positions',
        'kael_on_top',
        'claire_top_inside',
        'kael_inside'
    ])
    mirari_sex_choices = SexChoiceSet('mirari_sex_choices', [
        'top_choice',
        'shoulder_massage',
        'nibbles',
        'foot_massage',
        'leg_massage',
        'butt_massage',
        'breast_massage',
        'on_sides',
        'mutual_touching'
    ])
    orias_sex_choices = SexChoiceSet('orias_sex_choices', [])

label splashscreen:
    scene white
    show sugarlogo at logo_center with dissolve
    pause (2.0)
    hide sugarlogo with dissolve
    return

label start:
    python:
        # -- Global variables in the store -----------------------------
        akki_name = '???'
        mirari_name = '???'
        kael_name = '???'
        orias_name = '???'
        claire_name = 'Claire'

        # The current day (influences scenes we get to see)
        scenes_seen = 0
        current_day = 1
        in_sex = False

        # Track the scenes we've seen
        akki_scenes = 0
        mirari_scenes = 0
        kael_scenes = 0
        orias_scenes = 0

        akki_sex_choices.reset()
        kael_sex_choices.reset()
        mirari_sex_choices.reset()
        orias_sex_choices.reset()
        # Persistent data that have an effect on the game
        # persistent.sexcomplete : Boolean - completed at least one route
        # persistent.censor_18 : Maybe Boolean - censor filter
        

    stop music fadeout 2
    play sound "assets/sfx/game_start3.ogg"
    scene warning with dissolve
    pause
    scene black with dissolve
    pause (0.2)
    scene bg bedroom_night with dissolve
    pause (0.3)
    play music music_tension

    #Resetting everybody's expressions and bases
    $orias.set_state(base="default", glasses="off", **Emotion.normal())
    $kael.set_state(base="default", glasses="off", **Emotion.normal())
    $mirari.set_state(base="default",**Emotion.normal())
    $akki.set_state(base="default", **Emotion.normal())

    #TESTING TUTORIAL SCREEN
    if not persistent.played_once:
        "It looks like it is your first time playing {b}Cute Demon Crashers!{/b} \nWould you like to see some tips on how to play?"
        menu:
            "Take me to the tutorial!":
                call screen tutorial
            "No, thank you.":
                pass
        "You can still see the tips in the Extras menu if you feel lost."    

    $ claire_name = renpy.input("What's your name?", default='Claire',length=12).strip()
    if claire_name == "":
        $ claire_name = "Claire"
    $ claire.set_state(base="lazy", **Emotion.normal())
    $ claire.set_state(emotion_base="small blush" ,eyebrows="inwards", eyes="closed")

    cl "..."
    $ claire.set_state(with_dissolve,mouth="lip bite")
    cl "...."
    "I feel a pleasant shudder throughout my body as I continue to stroke myself."
    cl "Nn..."
    play sound "assets/sfx/cell_vibrate.ogg"
    "The phone on my nightstand vibrates, ruining the moment. I let out a groan, but roll over anyway. Using my clean hand, I grab the device and read the display."
   
    ## Add cellphone screen here
    show phone at phone_pickup

    $ renpy.pause(0.2)
    show screen phone_message("Kelsey", "I'm having an awesome time with my bf >o<b we just arrived in mexico sooooo romantic!")
    $ renpy.pause()

    hide screen phone_message
    $ renpy.pause(0.1)

    show screen phone_message("Chelsea", "OMG jelly. well i'm going 2 a party this wkend and gonna snag myself a hottie <3")
    $ renpy.pause()

    hide screen phone_message
    $ renpy.pause(0.1)

    show screen phone_message("Elsie", "guess who's celebrating their 2 week anniversary with her GF. This one /o/")
    $ renpy.pause()

    hide screen phone_message
    hide phone

    $renpy.pause(0.2)
    
    
#    "Kelsey: Picture attached. I'm having an awesome time with my bf >o<b we just arrived in mexico sooooo romantic!"
#    "Chelsea: OMG jelly. well i'm going 2 a party this wkend and gonna snag myself a hottie <3"
#    "Elsie: guess who's celebrating their 2 week anniversary with her GF. This one /o/ "

    $ claire.set_state(emotion_base="default", mouth="uhh", emotion="sigh", eyes="flat")
    cl "..."
    
    ##Hide cellphone screen

    "Usually I'd be happy for them, but for some reason, reading the friend chat is depressing. I sigh and lay back on the bed, pushing away the trashy romance book I read earlier."
    "It falls over, landing next to a few other books, my handheld device... and maybe a few forgotten plates and cups."

    $ claire.set_state(mouth="low", eyes="flat", emotion="default", emotion_base="dark")

    cl "It's spring break and here I am alone. I don't think I've even been outside since it started."
    $ claire.set_state(with_dissolve,mouth="wavy", eyes="flat", emotion="sweat")
    cl "My parents are on their yearly honeymoon and my little brother is away at baseball camp. All I have are my textbooks and, well, my right hand..."
    $ claire.set_state(with_dissolve,emotion_base="default", mouth="uhh", emotion="sigh", eyes="closed")

    "I close my eyes, no longer in the mood."
    cl "It would be nice just to have a little romantic fling..."

    stop music

    $persistent.played_once = True
    play sound "assets/sfx/scratch.ogg"
    "???" "I could help with that!"
    $mirari.set_state(with_dissolve, eyes="default", emotion="flowers")
    show mirari at center_alone with dissolve

    # [TODO] could have transforms applied to Claire's side sprite
    #        might require making ComposedSprite a displayable or something

    $ claire.set_state(mouth="fun ah", eyes="big", emotion="shock", emotion_base="no nose", eyebrows="up")
    cl "W-whaa!"
    play music music_silly
    $mirari.set_state(with_dissolve, mouth="low", eyebrows="inwards", eyes="dots", emotion="sweat")
    show mirari at center_group with dissolve
    "I jolt upward, causing the speaker to jump back."
    "???" "I guess that's a no?"
    $ claire.set_state(mouth="fun ah2", eyes="shock", emotion_base="no nose", eyebrows="frown", emotion="shiver")
    cl "M-more like what are you doing here in my house!?"
    cl "How did you even..."
    $akki.set_state(eyebrows="one up", mouth="neutral", emotion="small blush")
    $kael.set_state(eyebrows="inwards", mouth="neutral")
    show mirari at left4 with move
    show akki at mleft4
    show kael at mright4
    show orias at right4
    with moveinright

    $ claire.set_state(with_dissolve, **Emotion.shock())

    cl "..."
    cl "...WHAT'S GOING ON!?"

    $akki.set_state(with_dissolve,emotion="sweat", mouth="low", eyes="dots")
    show akki at sway
    ak "Huh? What {i}is{/i} going on?"
    $orias.set_state(with_dissolve,eyebrows="inwards", eyes="closed", emotion="sweat")
    ori "Oh, dear... Mirari, you didn't..."
    $mirari.set_state(with_dissolve, mouth="wah", eyes="clench", emotion="panic")
    show mirari at sway
    mi "I-I was going to explain in a bit! You guys arrived too fast!"
    $akki.set_state(mouth="ehh", eyebrows="frown", eyes="shock")
    show akki at bounce_up
    ak "How could we not when you conjured a portal RIGHT IN THE HALLWAY?" 
    voice "k_s01"
    $kael.set_state(with_dissolve, emotion="sweat", mouth="ah")
    ka "Ah, Miss, we mean you no harm. There already seems to be a misunderstanding on our part, and I apologize for the confusion. Um..."
    show kael zorder 3 at speak with None
    "He takes a step closer and I pull the sheets up to my chest. The bottom is snagged under the mattress, causing it to slip under my fingers, revealing my front."
    $mirari.set_state(emotion="sweat", mouth="low", eyes="default")
    $akki.set_state(emotion="bars", eyes="default", mouth="happy", eyebrows="up")
    show akki at bounce_up
    ak "I like your panda shirt."
    $ claire.set_state(**Emotion.normal())
    $claire.set_state(eyes="happy", mouth="happy")
    cl "Oh thanks, I got it at—"
    $ claire.set_state(with_dissolve, **Emotion.shock())
    $akki.set_state(with_dissolve, eyebrows="inwards", mouth="low", emotion="default")
    $claire.set_state(eyebrows="frown")
    extend " HEY, DON'T CHANGE THE SUBJECT. I'm not lowering my guard." 
    voice "k_w01"
    $kael.set_state(with_dissolve, eyes="happy", mouth="default")
    ka "Right. I think I would be terrified too, if four strangers suddenly showed up in my house."
    $claire.set_state(emotion="default", mouth="wavy", emotion_base="dark")
    cl "..."
    $claire.set_state(with_dissolve ,mouth="fun ah2")
    cl "Out!"
    $mirari.set_state(with_dissolve, eyes="bugteary",mouth="low", emotion="default")
    $akki.set_state(with_dissolve, eyes="bugteary",mouth="low", emotion="default")
    $kael.set_state(with_dissolve, eyes="default",mouth="low", emotion="default")
    $orias.set_state(with_dissolve, eyes="default",mouth="neutral", emotion="default")

    mi "Without even an explanation?" 
    cl "Ugh, fine, OUT into the hallway then! Please let me change first."
    play sound "assets/sfx/im_outa_here.ogg"
    hide mirari
    hide akki
    hide orias
    hide kael
    with moveoutright
    

    $claire.set_state(with_dissolve ,eyes="dizzy", mouth="wavy", eyebrows="inwards", emotion="shiver")

    cl "What the devil was that? They just appeared out of nowhere!"

    menu:
        "Call the police.":
            $claire.set_state(eyes="dots", mouth="wavy", eyebrows="frown", emotion_base="dark", emotion="sweat")
            cl "Only one way to handle a situation like this."
            cl "Hello? Police? Yeah, I'd like to report a break and enter..."
            #sirens and you got the "Arrested Some Cosplayers" ending!"
            scene black with dissolve
            play sound "assets/sfx/police_siren.ogg"
            pause(0.5)
            "You got the 'Arrested Some Cosplayers' ending!"
            return
        
        "Listen to them at the door first." :
            #[TODO]
            #Figure out what to do with the music for the rest of the scene
            "I approach the door and hold my ear close to the frame. They're not even trying to lower their voices, making it easy to catch every word." 
            ka "...We completely scared that poor girl, Mirari."
            voice "m_s18"
            ak "Ah, Kael's mad... he's never mad..."
            ori "This is why it's important to plan in advance..."
            voice "m_w02"
            mi "I know! I'm sorry! I just... took action without really thinking... I only wanted to help her... I feel awful now..."
            voice "k_s18"
            ka "Should we try talking to her once she calms down? We can at least apologize."
            "It truly does sound like there's a misunderstanding going on... Maybe they aren't that bad...?"
            $claire.set_state(eyebrows="inwards", eyes="closed", emotion="sweat", mouth="wavy")
            cl "I... can't believe I'm doing this, but I'll talk to them. Maybe there's a logical explanation behind all this..."
            $claire.set_state(with_dissolve, eyes="fun side", eyebrows="flat")
            cl "Yeah right."
            stop music fadeout 1
            jump start_hallway
    
label start_hallway:
    scene black with dissolve
    pause (0.1)
    play music music_tension
    scene bg hallway_night
    with dissolve
    pause (0.3)
    $akki.set_state(eyes="default")
    $mirari.set_state(eyes="default")
    $orias.set_state(eyes="closed")
    show mirari at left4
    show akki at mleft4
    show kael at mright4
    show orias at right4
    with dissolve

    $ claire.set_state(base="default", **Emotion.normal())
    $ claire.set_state(eyebrows="frown", mouth="wavy", emotion="sweat")
    cl "..."
    "Everyone" "..."
    show mirari zorder 3 at speak
    mi "Have you calmed yourself down?"
    $ claire.set_state(mouth="low")

    cl "As calm as I can be after having four strangers break into my bedroom..."
    $ claire.set_state(with_dissolve ,eyebrows="flat", mouth="uhh")
    cl "...with horns, and very revealing clothes..."
    cl "...Are you cosplayers?"
    $mirari.set_state(with_dissolve, eyes="default", mouth="default")
    show mirari at bounce_up
    voice "m_w03"
    mi "Cosplayers...? And we won't be strangers anymore if we give you our names!"
    show mirari zorder 0 at endspeak
    $kael.set_state(mouth="default", emotion="sweat")
    show kael zorder 3 at speak
    voice "k_w02"
    ka "I agree, we should properly introduce ourselves." 
    voice "k_w03"
    ka "I'm Kael. I apologize for the commotion earlier, my friend here can be a little, uh, impulsive."

    $ kael_name = 'Kael'
    show kael zorder 0 at endspeak
    $mirari.set_state(eyes="happy")
    show mirari zorder 3 at speak
    voice "m_w04"
    mi "Eh-heh, I guess I did jump in a little too soon. I'm Mirari, but Mira is okay too~"

    $ mirari_name = 'Mirari'
    show mirari zorder 0 at endspeak
    $akki.set_state(eyebrows="tender", mouth="ah")
    show akki zorder 3 at speak
    ak "Akki. Sorry about surprising you earlier... I guess we were all a little surprised."

    $ akki_name = 'Akki'
    show akki zorder 0 at endspeak
    $orias.set_state(eyebrows="tender", eyes="default",mouth="neutral")
    show orias zorder 3 at speak
    ori "...Orias. Pleased to make your acquaintance. And you are...?"

    $ orias_name = 'Orias'
    
    cl "...[claire_name]."
    $ claire.set_state(with_dissolve,mouth="low")
    cl "...And please, tell me why you're here." 
    show orias zorder 0 at endspeak
    $ akki.set_state(with_dissolve, mouth="grin", eyebrows="default")
    show akki zorder 3 at speak
    ak "You don't recognize us? We're incubi!"
    $mirari.set_state(eyebrows="default", eyes="default")
    show mirari at bounce_up
    voice "m_s07"
    mi "*cough* And one succubus." 
    cl "Incub...? Encubes? Wait, like the sex demons?" 
    $ claire.set_state(with_dissolve ,eyes="wide", eyebrows="up", emotion="panic", emotion_base="large blush", mouth="ehh")
    cl "Oh god, my fun times didn't attract you or something, did it?"
    $ claire.set_state(with_dissolve, mouth="low", emotion="default", eyes="tender side", emotion_base="small blush", eyebrows="inwards")
    cl "...I admit how you got into the house baffles me but I don't believe..."

    hide mirari
    hide kael
    hide akki
    hide orias
    with dissolve
    show portal with dissolve
    play sound "assets/sfx/portal_hum3.ogg"
    "I glance past them and see a giant swirling purple vortex hovering in the hallway. Okay, I'm convinced. It's a dream."
    $claire.set_state(eyes="mortified", emotion="shiver", eyebrows="inwards", emotion_base="default")
    cl "...You won't do anything bad to me?"

    hide portal
    $akki.set_state(emotion="panic", eyes="wide", eyebrows="inwards", mouth="ah")
    $mirari.set_state(emotion="sweat", mouth="oh", eyebrows="inwards")
    $kael.set_state(mouth="low")
    $orias.set_state(eyebrows="inwards")
    show mirari at left4
    show akki at mleft4
    show kael at mright4
    show orias at right4
    with dissolve
    show akki zorder 3 at speak
    ak "Whoa whoa, we'd never think of anything like that!" 
    $akki.set_state(emotion="default", eyes="default", mouth="neutral")
    show akki zorder 0 at endspeak
    $kael.set_state(emotion="default", eyebrows="default", eyes="tender", mouth="default")
    show kael zorder 3 at speak
    ka "You can rest easy. We're here to help you."
    $claire.set_state(emotion="default", eyes="tender")
    cl "Help...?"
    show kael zorder 0 at endspeak
    $mirari.set_state(emotion="flowers", mouth="default", eyebrows="up")
    show mirari zorder 3 at speak
    voice "m_s08"
    mi "You were feeling lonely, right? And you were fantasizing about having a fling."
    $mirari.set_state(emotion="default")
    show mirari zorder 0 at endspeak
    $orias.set_state(eyes= "closed", mouth="oh", eyebrows="up")
    show orias zorder 3 at speak
    ori "You were right about calling us 'demons' though. We feed off the sexual pleasure from humans."
    $mirari.set_state(emotion="flowers", eyes="happy", mouth="happy")
    show mirari at bounce_up
    voice "m_s10"
    mi "So it's a win-win situation! You get to have a good time, and we get nourished." 
    $claire.set_state(emotion="panic", eyebrows="up", eyes="big", mouth="wah", emotion_base="large blush")
    $orias.set_state(mouth="neutral")
    $mirari.set_state(emotion="default", mouth="default")
    show orias at endspeak
    cl "B-but I don't even know you!? I-I can't just... accept an offer like that out of the blue!"
    $orias.set_state(mouth="oh", eyes="default")
    show orias at speak
    ori "Purple portal."
    $claire.set_state(emotion="sweat", mouth="ehh", eyes="flat", emotion_base="dark")
    cl "Or that." 
    $orias.set_state(mouth="default", eyebrows="default")
    show orias zorder 0 at endspeak
    show kael zorder 3
    $kael.set_state(with_dissolve, eyes="tender side", mouth="low", eyebrows ="inwards")
    voice "k_s14"
    ka "But she does bring up a point..."
    $orias.set_state(with_dissolve, eyes="closed", mouth="oh")
    show kael zorder 0
    show orias zorder 3 at bounce_up
    ori "Not every human feels comfortable copulating with a stranger. It needs to be a positive experience for her to obtain this 'win-win situation', as Mirari puts it." 
    show akki zorder 3
    $akki.set_state(eyebrows="inwards", emotion="sweat", mouth="low")
    ak "So what do we do now?"
    $claire.set_state(emotion_base="small blush", mouth="low", eyes="semi open", emotion="default", eyebrows="inwards")
    cl "..."
    show akki zorder 0
    $mirari.set_state(mouth="wavy", emotion="lll", emotion_base="dark", eyebrows="inwards")
    show mirari zorder 3 at sway
    voice "m_s03"
    mi "Ah, I kinda... conjured the multi-being portal and it took a lot of effort... It has to run its course anyway... It won't vanish until a few days have gone by."
    $mirari.set_state(emotion="bars", emotion_base="default", eyes="default", mouth="happy", eyebrows="up")
    show mirari at bounce_up
    voice "m_w05"
    mi "I know! We can stay here for a little while until you feel comfortable experimenting with any of us." 
    $kael.set_state(**Emotion.normal())
    show kael zorder 3 at speak
    $mirari.set_state(emotion="default", mouth="default")
    voice "k_w04"
    ka "If you still don't trust us, we can leave. I promise we won't pressure you to do anything while we're here." 
    show kael zorder 0 at endspeak
    $orias.set_state(eyebrows="tender", eyes="default", mouth="oh")
    show orias zorder 3 at speak
    ori "Does that sound acceptable?"
    $orias.set_state(mouth="neutral")
    $claire.set_state(eyes="tender side")
    cl "Um... as... acceptable as having four sex demons hanging around my house, I guess..." 
    "My mind is all jumbled. If it's a dream, it'll be easier to go along with it, and once I wake up - *poof* - I'll know this never happened."
    show orias zorder 0 at endspeak
    show mirari zorder 3 at speak
    $mirari.set_state(emotion="flowers", eyes="happy", mouth="happy")
    voice "m_w06"
    mi "Thank you! I promise you won't regret it, [claire_name]." 
    $mirari.set_state(emotion="default", mouth="smile")
    $akki.set_state(eyes="happy", mouth="grin", eyebrows="default", emotion="starry")
    show mirari zorder 0 at endspeak
    show akki zorder 3 at speak
    ak "Don't worry, we'll go easy on you since you're a virgin."
    $mirari.set_state(eyes="fun side", mouth="v", eyebrows="up", emotion="note")
    show mirari at bounce_up
    voice "m_s06"
    mi "If anything, you'll have to go easy on {i}him{/i}. He's inexperienced, too." 
    $akki.set_state(emotion="shock", eyes="big", mouth="fun ah", emotion_base="large blush")
    $kael.set_state(eyes="happy", eyebrows="inwards")
    $orias.set_state(eyes="closed", mouth="smile")
    show akki at bounce_up
    ak "W-what, you don't just tell people that!" 
    $claire.set_state(eyes="happy", emotion="sweat", eyebrows="inwards", mouth="smile")
    cl "Hehe."
    "Virgin incubus, yeeeep, gotta be a dream."
    $mirari.set_state(eyes="closed", mouth="default", eyebrows="up")
    show mirari zorder 3 at sway
    $akki.set_state(emotion_base="small blush", eyes="default", mouth="low", emotion="default")
    show akki zorder 0 at endspeak
    voice "m_s16"
    mi "Now that's settled... Ah, I haven't been to the human realm in a while! I think I'll take a walk outside~"

    hide mirari with moveoutleft

    $claire.set_state(emotion_base="default", eyes="wide", eyebrows="up", emotion="panic", mouth="oh")
    cl "Ah... but..."
    "I guess she'll be okay; it's a dream after all."
    $kael.set_state(**Emotion.normal())
    show kael zorder 3 at speak
    voice "k_w05"
    ka "I hate to impose, but may I ask where the kitchen is?"
    $claire.set_state(**Emotion.normal())
    $claire.set_state(mouth="low")
    cl "Um, that way."
    $kael.set_state(eyes="happy")
    voice "k_w06"
    ka "Thank you."
    $akki.set_state(eyes="happy", emotion_base="default", mouth="grin")
    show akki at bounce_up
    ak "Great! I'm starving."
    $orias.set_state(with_dissolve, eyes="side")
    ori "I think I'll brew a nice cup of tea, too..." 

    hide akki
    hide kael
    hide orias
    with moveoutright


    #off-screen
    ak "Hey, I found the video games! Wow, check out this collection!"
    voice "k_w07"
    ka "Akki, don't raid her house!"
    ori "Be sure to return everything to its proper place."
    $claire.set_state(eyes="flat", emotion="sweat", emotion_base="dark", eyebrows="flat", mouth="uhh")
    cl "...I'm going back to bed. No more romance novels for a LONG while." 
    stop music fadeout 1
    jump day1_morning
