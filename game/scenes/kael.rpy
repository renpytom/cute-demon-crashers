#--CG variations variables init--------
define kael_warmup_clface = "1"
define kael_warmup_kael = "1"
define kael_mis_clface = "1"
define kael_mis_kface = "1"
define kael_cuddle_clface ="2"
define kael_cuddle_kface ="2"
define kael_naked = False
define kael_claire_naked = False
define kaeloral = False
define kaelfinger = False
define pillowrecall = False
define tenderactivity = False
define sillyactivity = False
define tenderrecall = False
define kissingactivity = False
define kissinghimactivity = False
define undressingtime = False
define oral2 = False
define fingers2 = False
define kaelontop = False
define kaelinside = False
define kael_cutin = False
define kael_epilong = False




label kael_hangout1:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_kael
    $kael.set_state(base="default",**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    scene bg hallway_day with dissolve
    $claire.set_state(eyebrows="up", mouth="uh")
    cl "What is he doing...?"
    if current_day == 1:
        cl "Cooking and now cleaning..."
    cl "Kael?" 
    show kael at center_alone2 with dissolve   
    "He pauses and adjusts the overflowing laundry basket in his arms."
    show kael at bounce_up_alone2
    voice "k_w16"
    ka "[claire_name], can I help you?"
    $claire.set_state(eyebrows="flat", emotion="sweat", mouth="smile")
    cl "Um... I was wondering why you were doing the laundry."
    $kael.set_state(with_dissolve, emotion="bars", mouth="ah", eyebrows="up")
    ka "Oh."
    "He sets the basket down, and pulls out a note tucked by his hip. I accept it, instantly recognizing the handwriting."
    $kael.set_state(with_dissolve,**Emotion.normal())
    "'PLEASE PLEASE do your laundry while we're gone! Love, Mom'"
    $claire.set_state(emotion="lll", emotion_base="dark", eyes="flat")
    cl "..."
    "Now I remember. My parents left a few (too many) memos posted on the fridge. I guess he noticed when he made breakfast..."
    $kael.set_state(with_dissolve,emotion="default", eyebrows="default", eyes="happy", mouth="smile")
    ka "I thought, since we're here and all, I could help out since you've fallen behind."
    $kael.set_state(with_dissolve, eyebrows="inwards", eyes="default", mouth="neutral")
    ka "How long have your parents been gone? Over a week I assume from the clothes."
    $claire.set_state(mouth="smile", eyes="fun side")    
    cl "They left only a few days ago."
    $kael.set_state(with_dissolve, emotion_base="dark", eyes="fun front", mouth="low", eyebrows="default")
    ka "..."
    $claire.set_state(eyes="flat", mouth="uhh", eyebrows="inwards", emotion="sigh")
    cl "I know, I know, I've been a slob."
    $kael.set_state(with_dissolve, eyes="closed", emotion_base="default", eyebrows="one up", mouth="fun smile")
    ka "Being genuinely lazy or has something been bothering you?"
    $claire.set_state(eyes="tender side", mouth="low", emotion_base="default", emotion="default")
    cl "I shouldn't excuse my behaviour, but yeah it's a bit of the latter..."
    $claire.set_state(with_dissolve, eyes="down", mouth="oh")
    cl "I've mostly been studying and neglecting the chores." 
    $claire.set_state(with_dissolve, eyes="flat", mouth="low")
    cl "I feel all I've been doing lately is hitting the books..."
    $kael.set_state(with_dissolve, eyes="default", emotion_base="default", mouth="low", eyebrows="up")
    voice "k_s16"
    ka "Hm?"
    $claire.set_state(emotion="sweat", eyes="happy", mouth="smile")
    cl "Ah, sorry, it's, well... University hasn't been turning out as fun as I hoped. And now all my friends are out there, dating or meeting people this spring break." 
    $claire.set_state(with_dissolve, eyes="fun front", eyebrows="flat", mouth="uhh", emotion_base="dark")
    $kael.set_state(with_dissolve, eyebrows="inwards")
    cl "I thought maybe I just need a little family time instead. Of course as soon as I come back, my parents are on a lovely-dovey trip to Mexico and my brother's at baseball camp with his teammates." 
    $kael.set_state(with_dissolve, eyes="happy", mouth="smile", emotion="sweat")
    $claire.set_state(with_dissolve, eyes="fun side", mouth="pout")
    cl "Everyone has plans but me."
    "I let out a self-deprecating laugh, but it comes out more bitter than I expect."
    "I shove the note into my pocket and Kael gives a thoughtful nod."
    $kael.set_state(with_dissolve, eyes="tender", emotion="default", mouth="neutral")
    voice "k_s06"
    ka "I can't say I know much about this university or spring break thing... but I know what it's like to feel alone."
    $kael.set_state(with_dissolve, emotion="note", eyes="default", mouth="smile", eyebrows="default")
    voice "k_w18"
    ka "It's not much, but I'll do what I can to get you back on your feet at least. Maybe you'll feel better once the house is clean and it gives you a peace of mind."
    $kael.set_state(with_dissolve, emotion="default", eyes="wink", mouth="happy")
    voice "k_w19"
    ka "Besides, you have four people hanging around. Can't be that lonely now, right?"
    $kael.set_state(with_dissolve, eyes="closed", mouth="ah", eyebrows="up")
    ka "Of course, I expect you to pick up the slack. I'm an incubus, not your mom." 
    $claire.set_state(mouth="vhappy", eyes="happy", emotion_base="default", emotion="flowers", eyebrows="inwards")
    cl "...Hahaha. I never thought I'd hear an incubus say that."
    $kael.set_state(with_dissolve, eyes="up", mouth="low")
    voice "k_w21"
    ka "...Believe me, that's not the first or last time I'll say those words to someone. Blame my being a stickler for cleanliness." 
    $claire.set_state(emotion="default", eyes="tender", eyebrows="flat", mouth="uh")
    cl "You're not trying to butter me up or earn points or something, right?"
    $kael.set_state(with_dissolve, eyebrows="default", mouth="smile", eyes="closed")
    "He shakes his head, then picks up a discarded sock forgotten in the hallway. Why is there only one sock, though...?"
    $kael.set_state(with_dissolve, eyes="tender")
    stop music fadeout 2
    voice "k_w22"
    ka "I'm simply being me. We all are. We'd like you to feel comfortable around us; there's no point in being dishonest about who we are." 
    hide kael with dissolve
    show chibi_kael01 at chibi_scene with dissolve
    play music music_silly fadein 2
    "He picks up the basket, and it's then I spot some lacy underwear on the pile."
    cla "Ah, I'll wash those!"
    "I grab my unmentionables, and Kael looks at me in surprise."
    voice "k_w23"
    ka "Really? Well, if you dig through the pile there's more—"
    cla "WHAT!?"
    cla "I-I'll do my personal load! Come back in a few minutes once I gather them. I can at least do that!"
    voice "k_w24"
    ka "Deal."
    hide chibi_kael01 with dissolve
    stop music fadeout 2

    jump next_day


label kael_hangout2:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    scene bg living_room with dissolve
    $kael.set_state(base="default",**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    $renpy.pause(0.4)
    
    scene bg living_room with dissolve
    play sound "assets/sfx/glass_crash.ogg"
    "Crash!"
    $claire.set_state(eyes="wide", eyebrows="up", mouth="wavy", emotion="shock")
    cl "What was that?"
    play music music_kael fadein 2
    $kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="low" )
    show kael at center_alone2 with dissolve
    "I hurry to the living room and spot Kael staring at the floor with wide eyes."
    $kael.set_state(eyebrows="inwards", emotion="panic", mouth="ehh")
    "There's a shattered picture frame with pieces of glass scattered before the fireplace. Kael kneels down, his hands hovering over the mess, wondering what to do." 
    $claire.set_state(eyebrows="inwards", mouth="oh", emotion="default", eyes="default")
    cl "What happened?"
    show kael at sway
    $kael.set_state(eyes="bigcry", mouth="wah", emotion_base="no nose")
    voice "k_w25"
    ka "[claire_name], I apologize! I was dusting the mantle and this frame tipped over..."
    show kael at sway
    $kael.set_state(with_dissolve, eyes="clench")
    voice "k_s13"
    ka "Careful, I don't want you to cut yourself."
    $kael.set_state(with_dissolve,emotion="default", mouth="wavy", eyes="default", emotion_base="default")
    "I crouch down beside him and gingerly pluck out the photograph. It's an old picture of my family standing in front of a twisty arbutus tree from some park." 
    $kael.set_state(with_dissolve,eyebrows="default", mouth="low")
    "Kael peers at it, curious."
    $kael.set_state(with_dissolve,mouth="ah", emotion="bars", eyebrows="up", eyes="wide")
    voice "k_w26"
    ka "Is... that... you?"
    $claire.set_state(eyebrows="inwards", mouth="smile", eyes="tender")
    cl "Yes, when I was ten. This is my mom, dad, and the one in the dinosaur jacket is my little brother when he was four." 
    $kael.set_state(with_dissolve, emotion="default", eyes="default", eyebrows="default", mouth="happy")
    voice "k_w27"
    ka "Fascinating... You look so different. Smaller frame and knobby knees."
    $claire.set_state(eyebrows="flat", mouth="uh", eyes="default")
    cl "Huh? Well yeah, I was a kid. Then I grew up. Is it the same for incubi and succubi?"
    $kael.set_state(with_dissolve, eyes="closed", mouth="smile")
    voice "k_w28"
    ka "Not at all. When we're, um, 'born', we're already as we are. I've always found the human nuclear family interesting since we don't have our own."
    $kael.set_state(with_dissolve, eyes="tender")
    ka "We also live alone for the most part. It's rare for our kind to stay together."
    $claire.set_state(eyebrows="up")
    cl "Then... what about you, Akki, Orias and Mirari? How did you all get acquainted?" 
    $kael.set_state(with_dissolve,eyes="closed", mouth="happy")
    ka "I found Orias and Mirari passed out and injured while I was exploring a forest in the demon world."
    $claire.set_state(mouth="uhh", emotion="sweat")
    cl "What happened? Were they okay?"
    $kael.set_state(with_dissolve, eyes="happy", emotion="sweat", eyebrows="inwards", mouth="smile")
    ka "Yes. As soon as I patched them up, they jumped into the fray again... They were, uh, rather vehement in taking down a monstrous flower."
    $claire.set_state(eyes="dots", mouth="oh", eyebrows="inwards")
    cl "Mirari I can imagine, but Orias?"
    $kael.set_state(with_dissolve, eyes="wink", mouth="grin")
    ka "He can be stubborn when it comes to creating new tea blends... Of course, I didn't know that at the time." 
    $kael.set_state(with_dissolve, **Emotion.normal())
    ka "We stuck together after that. Someone has to make sure those two stay out of trouble." 
    $claire.set_state(eyes="happy", eyebrows="default", mouth="smile", emotion="default")
    cl "Hehe, and Akki?"
    $kael.set_state(with_dissolve, emotion="default", mouth="ah", eyebrows="up")
    ka "He's the youngest incubi I know of. When we're born, aside from basic knowledge of our identity and how to survive, we're essentially a blank slate."
    $kael.set_state(with_dissolve, eyes="wink", mouth="smile", eyebrows="default")
    ka "After we found him, we took him under our wing. He's still learning how to use his powers and it's his first time in the human world. Keep it a secret, but he's easier to manage than the other two."
    $kael.set_state(with_dissolve, eyes="happy", emotion="note")
    ka "That's my 'family' for you."
    cl "Aw, it's a wonderful family. I'm pretty close to my parents, although my brother can be a brat when he hogs all the video games and saves over my files." 
    "Still, I glance fondly at the photograph."
    $kael.set_state(with_dissolve, eyebrows="inwards", eyes="dots", mouth="low", emotion="lll", emotion_base="dark")
    voice "k_w29"
    ka "Again, sorry about the mess..."    
    $claire.set_state(eyebrows="inwards", emotion="sweat", eyes="default")
    cl "Don't worry, it'd be believable that I accidentally knocked it over. I think my parents will be more surprised over a tidy room than a broken frame."
    $claire.set_state(with_dissolve, eyes="happy", emotion="default", eyebrows="default")
    cl "I can buy another one later, anyway. I'll grab a broom."

    jump next_day


label kael_hangout3:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $kael.set_state(base="default",**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    $renpy.pause(0.4)
    play music music_kael
    scene bg kitchen with dissolve
    play sound "assets/sfx/chopping.ogg"
    $claire.set_state(eyes="flat", mouth="pout", emotion_base="dark", eyebrows="frown", emotion="lll")
    cl "Twenty minute stir-fry my butt. It's taking me ten to chop veggies." 
    "I glance at the instructions saved on my phone and continue slicing a large carrot." 
    $kael.set_state(eyebrows="up", mouth="ah")
    show kael at center_alone2 with dissolve
    voice "k_s09"
    ka "Oh? This is a surprise. You can cook?"
    $claire.set_state(eyebrows="inwards", mouth="low", eyes="tender side", emotion="sweat", emotion_base="small blush")
    cl "Not at all, but when I see you doing all my chores around the house... I couldn't just laze around doing nothing."
    $claire.set_state(with_dissolve, eyes="default", mouth="smile", emotion_base="default")
    cl "I thought maybe I could step in and cook a decent meal at least."
    $claire.set_state(with_dissolve, mouth="happy", eyebrows="default", eyes="happy")
    cl "Um, thanks for that. I think it was the push I needed to start being more proactive." 
    $kael.set_state(with_dissolve, emotion="flowers", mouth="happy", eyes="happy")
    voice "k_w30"
    ka "I'm glad. Do you want me to help you prep the ingredients at least?"
    cl "Nah, I got this, honest I—"
    stop music fadeout 3
    "Do carrots normally ooze red juice when cut?"
    hide kael with dissolve
    show chibi_kael02 at chibi_scene with dissolve
    #$claire.set_state(eyes="dots")
    cla "..."
    play music music_silly fadein 2
    #$claire.set_state(with_dissolve, eyes="big", mouth="fun ah", emotion="shock", eyebrows="inwards", emotion_base="dark")
    cla "OW! FRICK!" 
    #$kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="shock")
    voice "k_w31"
    ka "Are you okay?"
    "He rushes to my side as I examine my injured finger. He reaches to have a look at it, but I hold the wound close to my chest."
    hide chibi_kael02
    $kael.set_state(emotion="panic", mouth="wah", eyes="big", eyebrows="inwards", emotion_base="dark")
    show kael at center_group with dissolve
    "Kael seems confused but steps back to give me room. If anything, he's panicking more than me."
    $kael.set_state(with_dissolve, eyes="dots", mouth="wavy", emotion="sweat lots")
    voice "k_w32"
    ka "It's okay, I know how human bodies work. One minor cut and it's fatal unless treated. Do you have a medical kit?"
    $claire.set_state(emotion="sweat", eyes="happy", mouth="smile", emotion_base="default")
    stop music fadeout 2
    cl "I don't think it's that serious... but the first-aid kit should be beside the fridge." 
    play music music_kael fadein 2
    $kael.set_state(with_dissolve, eyes="default", emotion="default", mouth="low", emotion_base="default")
    "He urges me toward the counter, and I sit on its surface while he rummages through the kit."
    "He pokes around the supplies and selects what he needs."
    $claire.set_state(eyebrows="up", eyes="default", mouth="uh", emotion="default")
    cl "You seem familiar with human medicine; I'm impressed."
    $kael.set_state(mouth="neutral")
    show kael at center_alone2 with dissolve
    "He applies a clean disinfecting wipe to my finger, and I bite my lip from the slight pain."
    $kael.set_state(with_dissolve, mouth="smile", eyes="tender")
    ka "It's something I picked up whenever I stayed in the human world."
    $kael.set_state(with_dissolve, eyebrows="default")
    ka "The med— first-aid kits may change appearances over the years, but the contents and uses are roughly the same." 
    $kael.set_state(with_dissolve, eyebrows="inwards", mouth="grin", eyes="happy")
    ka "Although the band-aids usually don't have dinosaur patterns." 
    $kael.set_state(with_dissolve, emotion="note", eyebrows="up", eyes="default", mouth="happy")
    voice "k_w33"
    ka "Ta-da, you're good to go."
    "I wiggle my newly bandaged finger."
    $claire.set_state(eyebrows="inwards", mouth="smile")
    $kael.set_state(with_dissolve, **Emotion.normal())
    cl "Thanks... Sorry about keeping my hand away from you earlier."
    $claire.set_state(emotion="sweat", eyes="happy")
    cl "I thought you were gonna do something weird like suck the blood or stick it in your mouth, being a demon and all."
    $kael.set_state(with_dissolve, eyebrows="one up", eyes="fun front", mouth="ah")
    ka "I'm not a vampire. I don't go around sticking bloody, onion-smelling fingers into my mouth. It's not sanitary." 
    $kael.set_state(with_dissolve, eyes="closed", mouth="smile")
    voice "k_s20"
    "He holds up my hand and teasingly nibbles a knuckle, making me giggle."
    $claire.set_state(mouth="happy", eyes="clench", emotion_base="small blush")
    cl "I'm sorry."
    $kael.set_state(with_dissolve, eyes="tender", eyebrows="frown")
    ka "And I guess you expected me to do this next, right?"
    "He leans in, then delivers a cold puff of air to my neck. The ticklishness catches me by surprise and I squeal, falling back." 
    stop music fadeout 2
    $claire.set_state(eyes="wide", eyebrows="up", mouth="oh", emotion="default")
    cl "Oh—"
    play music music_romance fadein 2
    show kael at bounce_down_alone2
    $kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="shock")
    voice "k_s07"
    ka "Whoa—"
    "He wraps his arms around my back and pulls me close. My chin rests on his shoulder and I can feel my face warming up from the contact."
    $kael.set_state(with_dissolve, emotion="sweat", eyes="tender", eyebrows="inwards", mouth="smile")
    ka "Um, I apologize. I went too far with that joke..."
    $claire.set_state(emotion_base="large blush", eyes="down", eyebrows="inwards", mouth="smile")
    cl "I-it's okay..."
    hide kael with dissolve
    "We separate, and Kael immediately busies himself by packing up the kit. I hop off the counter and resume cutting veggies, albeit cautiously." 
    $kael.set_state(**Emotion.normal())
    $kael.set_state(eyes="wink")
    show kael at center_alone2 with dissolve
    ka "Want me to help with your meal? You'll learn faster that way. You'll still do most of the work, of course."
    $claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion_base="default", emotion="sweat")
    cl "Deal. I don't want to have four demons keel over from food poisoning; it'd be improper hosting." 
    $kael.set_state(with_dissolve, eyes="happy", mouth="happy")
    voice "k_s04"
    "He laughs and starts washing the broccoli. For a few minutes, there's a comfortable silence between us."
    $kael.set_state(with_dissolve, eyes="tender", emotion="heart", mouth="smile", emotion_base="small blush")
    ka "[claire_name], if you happen to pick me tonight... I'd like that. I promise to make your spring break a memorable one." 
    $claire.set_state(emotion_base="large blush", eyes="tender", eyebrows="inwards", mouth="smile", emotion="default")
    cl "Thank you..."

    jump next_day
    

label kael_sex:
    $ in_sex = True

    if _in_replay:
        $ sex_stop_label = "kaelstoppingnow"
        show screen replay_controls()

    if not _in_replay:
        $ persistent.kael_claire_name = claire_name
        $ persistent.kael_scenes = kael_scenes
    
    stop music fadeout 2
    scene black with dissolve
    $renpy.choice_for_skipping()
    pause(0.5)
    play music music_tension
    scene bg hallway_night with dissolve
    $ kael_cuddles_sprite.set_state(**kael_cuddles_initial)
    $ kael_warmup_sprite.set_state(**kael_warmup_initial)
    $ kael_missionary_sprite.set_state(**kael_missionary_initial)
    $kael.set_state(**Emotion.normal())
    $ claire.set_state(**Emotion.normal())
    $ claire.set_state(base="chemise", emotion_base="large blush", mouth="wavy", eyebrows="flat")

    cl "Here I go..."
    play sound "assets/sfx/knock.ogg"
    "I knock on the bedroom door, which is already slightly open." 
    $claire.set_state(eyes="tender", mouth="uh", eyebrows="inwards")
    cl "Kael, are you in there? Can I enter?"
    voice "k_sex01"
    ka "Feel free."
    scene bg bedroom_night with dissolve
    "Inside, I can hear the soothing backdrop of soft classical music. I guess he figured out how to work my neglected CD player..." 
    $kael.set_state(eyes="tender", emotion_base="small blush", mouth="smile")
    show kael at center with dissolve
    show kael at center_alone2 with dissolve
    $kael.set_state(emotion="heart")
    voice "k_sex02"
    ka "You look adorable, [claire_name]."
    "I approach him and he takes my hand, raising it over my head. Coupled with the music, I take the cue and give a little twirl." 
    $kael.set_state(emotion="note", eyes="wink", mouth="grin")
    voice "k_s04"
    ka "Blue is a lovely colour on you, but that could just be my bias." 
    $claire.set_state(eyes="tender", emotion_base="small blush", emotion="default", eyebrows="default", mouth="smile")
    cl "Thank you, Kael..." 
    "He guides me to the middle of the bed and makes himself comfortable on his knees. I hesitantly follow suit."
    hide kael with dissolve
    show kael_start with dissolve
    voice "k_sex03"
    ka "Still nervous?"
    cla "Yeah. I think it's mostly the, uh, experience gap."
    voice "k_s19"
    ka "Since this is your first time, we'll focus on you."
    voice "k_sex04"
    ka "Just be honest about how you feel and I'll do my best. If there's anything you want to try or do, let me know."
    cla "A-anything? W-well since this is my first time... I'm not even sure what I'd like or dislike, myself..."
    voice "k_sex05"
    ka "Exploring is part of the process. We'll take it slow."
    voice "k_s03"
    ka "Unless you prefer something more playful, like a pillow fight."
    "I laugh, but I get the feeling he's completely serious, too." 
    cla "Thanks for easing my mind."
    voice "k_sex06"
    ka "No problem. I want it to be a fun experience for you."
    "How should we start...?"
    stop music fadeout 2
    menu:
        "Slow and gentle.":
            $ tenderactivity = True
            $ tenderrecall = True
            play music music_love fadein 3
            cla "Slow sounds like a perfect way to start."
            "He leans in and gives me a gentle kiss on the forehead."
            voice "k_sex08"
            ka "Of course."
            show kael_start hand with dissolve
            show screen sex_stop("kaelstoppingnow")
            "He takes my hand and brings it up to his face, giving me a fond smile before delivering light kisses to my fingers. The sight makes my heart flutter as well, as his moist lips travel up my hand."
            "His hand moves to cup my cheek, stroking it with his thumb. He gazes tenderly at me before closing the distance, his lips meeting mine." 
            show kael_start kiss with dissolve
            "At first the kisses are quick tastes, lightly brushing the surface, then gradually deepening once I tilt my head and welcome a firmer approach. When our lips lock, I inhale sharply, taking in his earthy scent." 
            "I wrap my arm around him, cradling my hand under his head to encourage him and he responds mutually by running his fingers through my hair."
            hide kael_start with dissolve
            show kael_leaning with dissolve
            "He gently lowers my body to the bed, positioning himself over me. Smiling, he brushes my bangs aside then playfully nuzzles my nose with his as our foreheads touch." 
            "It's then I realize all my anxiety is gone, melted away thanks to his tenderness." 
            jump kissingpermission
        #"Why not? Let's wrestle.":
          #  "That suggestion sounds so absurd, I can't pass it up." 
         #   cl "Sure, why not? We can wrestle."
          #   ka "Oh? You really want to try?"
            # cl "I... think I can take you on."
            # $ sillyactivity = True
            # $ wrestlerecall = True
            # "I widen my knees, then launch toward his torso, hugging him awkwardly. It's like trying to push down a stone wall." 
            # "He looks at me in bafflement, then bursts out laughing." 
            # "He makes a playful growl and reaches for me, but I scoot out of his reach, toward the other side of the bed. Kael is deliberately slow, but I still giggle victoriously when I successfully dodge him." 
            # "Finally I decide take the offense and lunge at him, grabbing his shoulders. He simply uses his weight and we topple over together, him hovering over me."
            # "We exchange amused glances then burst out laughing."
            # ka "I win."
            # cl "Only because I let you."
            # ka "If you say so."
            # "He nuzzles my nose affectionately before fixing my disheveled bangs. I'm winded from the activity, and I can feel my heart pounding frantically, my breathing shallow." 
            # "Not only that, I realize my anxiety has melted from the silliness. Kael straddles over me and touches his forehead against mine." 
            # jump kissingpermission
        "Pillow fight!!!":
            "Why not? I grab a pillow behind me."
            show kael_start pillow with dissolve
            $ pillowrecall = True
            $ sillyactivity = True
            cla "Then think fast!"
            voice "k_sex12"
            ka "Hu— Hey!"
            show screen sex_stop("kaelstoppingnow")
            "The pillow bounces off his face, and I laugh, amused by his slow reaction."
            cla "Take that!"
            "With my own pillow, I whack him in the shoulder. He shuffles out of the way in time for my second attack to hit the bed. He retaliates with a light blow to my back."  
            voice "k_sex13"
            ka "Likewise."
            cla "I'm just getting started."
            "We continue exchanging blows, with Kael more on the defense while I'm on the offense. He crawls over to the end of the bed, then lifts a pillow high above his head, readying for an attack."
            voice "k_sex14"
            ka "Prepare yourself— Oh—"
            cla "Careful!"
            hide kael_start with dissolve
            play music music_love fadein 3
            "He loses his balance, teetering too close to the edge. I hastily drop my pillow and cling to his waist, pulling him toward me instead." 
            voice "k_s05"
            "I land on the bed with a thud, Kael straddling me. We look at each other in surprise, then burst out giggling." 
            show kael_leaning with dissolve
            "My heart is beating wildly under my rib cage, and I'm sweaty and winded from the activity. I realize my anxiety has also melted away from the silliness."
            if kael_scenes >= 2:
                "I think back to the picture frame."
                cla "I'm... starting to suspect you're a little on the clumsy side."
                voice "k_sex15"
                ka "Me? For all you know it could've been a part of my plan to get closer to you."
                cla "Well, it worked, intentional or not."
            "Kael leans in and nuzzles my nose, his hand seeking my own. Our fingers intertwine, and he gives my forehead a gentle kiss."     
            jump kissingpermission
        "Maybe I'm not ready...":
            hide screen sex_stop
            cla "Um, I don't think I'm ready after all.."
            cla "Sorry."
            hide kael_start with dissolve
            $kael.set_state(**Emotion.normal())
            $kael.set_state(eyebrows="inwards", mouth="smile", eyes="tender")
            show kael at center_alone2 with dissolve
            voice "k_sex07"
            ka "That's all right. You know yourself best."
            voice "k_s12"
            $kael.set_state(with_dissolve, eyebrows="up", eyes="default")
            ka "Would a cuddle suffice?"
            stop music fadeout 2
            cl "Yeah... I'd like that."
            scene kael_cuddles with dissolve
            play music music_lullaby fadein 2
            "I roll over and Kael hugs me from behind, his body pressing against mine. His breath warms the base of my neck, and the soft music drifts through the room." 
            "Relaxed and secure in his arms, I close my eyes and fall into a restful sleep." 
            call credits
            jump kael_epilogue

            
label kissingpermission:
    $ sillyactivity = False
    $ tenderactivity = False
    show kael_leaning b with dissolve
    voice "k_sex16"
    ka "Permission to kiss you all over?"
    cla "A-all over?"
    voice "k_sex17"
    ka "{i}All{/i} over." 
    menu:
        "Yes.":
            cla "P-permission granted..."
            hide kael_leaning with dissolve
            $kael.set_state(eyes="happy", mouth="grin", emotion_base="default", eyebrows="default", emotion="default")
            show kael at center_alone2 with dissolve
            $ kissingactivity = True
            voice "k_s04"
            "He chuckles at my formality, but plants a brief kiss on my forehead before withdrawing."
            hide kael with dissolve
            "He positions himself before my bent knees, and gives the top of my foot a tender kiss."
            $claire.set_state(eyebrows="up", eyes="wide", mouth="low")
            cl "You really meant it when you said all over..."
            $kael.set_state(eyes="wink", mouth="smile")
            show kael at center_alone2 with dissolve
            voice "k_sex18"
            ka "I like to keep my word."
            hide kael with dissolve
            "His lips flutter over my ankle and continue upward. The sensation makes me smile and I inhale deeply as he continues exploring my legs with the softest of kisses." 
            hide kael with dissolve
            show kael_kissing A2 with dissolve
            "When he reaches my knees, he rests his chin on them and gazes at me."
            cla "Something up?"
            voice "k_s18"
            ka "Taking a little break. Seeing how you're doing."
            "He gives my hand a gentle squeeze and I can feel myself blush."
            voice "k_sex19"
            ka "You're adorable." 
            cla "Thank you..."
            hide kael_kissing with dissolve
            "He resumes kissing my knees and coaxes them apart, his mouth continuing to my thigh. The closeness makes my stomach coil and I hold my breath in anticipation as his lips brush closer and closer to the top of my legs."
            "He pauses, then kisses below my navel instead."
            $kael.set_state(eyes="wink", emotion="heart", mouth="grin", emotion_base="default")
            show kael at center_alone2 with dissolve
            voice "k_s04"
            ka "I'll come back to this later~"
            $claire.set_state(eyes="clench", emotion_base="large blush", mouth="v", eyebrows="inwards")
            cl "You tease." 
            $kael.set_state(with_dissolve, eyebrows="one up", mouth="smile", emotion="default")
            voice "k_sex20"
            ka "Am I?"
            "Kael kisses above my navel, which I can feel through my chemise. He travels upward, then stops below my breasts. He crosses his arms there, then rests his chin on them, gazing at me fondly." 
            $kael.set_state(with_dissolve, eyebrows="default", eyes="tender")
            ka "I know this was short notice... being only a few days and all... but thanks for trusting me." 
            $claire.set_state(emotion_base="small blush", eyes="tender", eyebrows="inwards", mouth="smile")
            cl "Ah, no, I should thank you... Thanks for wanting to be with me." 
            $kael.set_state(with_dissolve, eyes="happy")
            voice "k_sex21"
            ka "Of course I'd want to." 
            "He kisses my forehead as his fingers graze lightly underneath my chest."
            voice "k_s14"
            $kael.set_state(with_dissolve, eyes="tender")
            ka "Would you like it if I kissed your breasts, too?"
            $claire.set_state(eyebrows="default")
            cl "Yes." 
            hide kael with dissolve
            show kael_kissing A1 with dissolve
            "He seals the affirmation with a deep kiss on my lips while intertwining our fingers together. When we part, he nuzzles my nose before exploring my neck, just under my earlobe." 
            "Traveling down my neck, he teases my sternum before caressing my breast with his hand. He takes a nipple into his mouth, gently sucking on it through the chemise."
            "He fondles me in circular motions, applying an occasional light squeeze while his thumb brushes over my erect nipple."
            "Even through the sheer fabric, his touch stirs something within me and I breathe in a longing sigh."
            "My head sinks deeper into the pillow. He repeats the treatment to my other breast before traveling back down to my navel." 
            "His lips graze over my stomach, up and then down, but gradually moving closer to the rim of my panties, and I realize what he's hinting at." 
            hide kael_kissing with dissolve
            show kael at center_alone2 with dissolve
            voice "k_sex22"
            ka "Should I keep going?"
            $ kissingactivity = False
            menu:
                "This is fine.":
                    $ kaeloral = True
                    $ undressingtime = True
                    $claire.set_state(emotion_base="large blush", eyes="tender", eyebrows="inwards", mouth="smile")
                    cl "Yes. Um, here..."
                    "I pull up my chemise, and his fingers slip under the strap of my panties, giving it a teasing tug." 
                    $kael_claire_naked = True
                    jump oralactivity
                "Request to use fingers instead.":
                    $ kaelfinger = True
                    cl "Um, is it okay if you use your fingers for the first time?"
                    $claire.set_state(emotion_base="large blush", eyes="tender", eyebrows="inwards", mouth="uh")
                    voice "k_sex23"
                    ka "I can do that."
                    $ undressingtime = True
                    "I pull up my chemise, and his fingers slip under the lace of my panties, giving it a teasing tug."
                    $kael_claire_naked = True
                    jump oralactivity
                "I'd like to stop now.":
                    hide screen sex_stop
                    $claire.set_state(emotion_base="large blush", eyes="tender", eyebrows="inwards", mouth="low")
                    cl "Um... Wait..."
                    $kael.set_state (with_dissolve, eyebrows="up", eyes ="default", mouth="low")
                    "I sit up and Kael moves back." 
                    voice "k_sex24"
                    $kael.set_state(with_dissolve, mouth="ah")
                    ka "Everything all right?"
                    $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low")
                    cl "Yes. I don't think I'm ready to go farther. Sorry if I ruined the mood..."
                    voice "k_s01"
                    $kael.set_state(with_dissolve, eyes="closed", mouth="smile")
                    ka "Not at all. Thank you for your honesty." 
                    voice "k_s12"
                    $kael.set_state(with_dissolve, eyes="wink", eyebrows="up")
                    ka "We can do something else, like cuddle." 
                    $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
                    cl "I'd like that..."
                    stop music fadeout 2
                    jump kaelearlystop
            
        "How about {i}I{/i} kiss you all over?":
            $ kissinghimactivity = True
            hide kael_leaning with dissolve
            $kael.set_state(with_dissolve, eyes="tender", eyebrows="default", emotion_base="default", emotion="default", mouth="smile")
            show kael at center_alone2 with dissolve
            $claire.set_state(eyes="down", mouth="v", eyebrows="up")
            cl "Um... I'd like to do this to you instead, if it's alright..."
            $kael.set_state(with_dissolve, eyebrows="up", eyes="default")
            voice "k_s10"
            ka "Oh?"
            $claire.set_state(eyes="clench", mouth="kitty", emotion_base="large blush", eyebrows="inwards")
            cl "Yes..."
            $kael.set_state(with_dissolve, eyes="wink", emotion="note", eyebrows="default")
            voice "k_sex26"
            ka "I'd like that."
            "He kisses my forehead, then hugs me close. He playfully rolls over until I'm the one over him."
            hide kael with dissolve
            show kael_kissing B with dissolve
            "I gaze down at him, unsure where to start now that I'm the one leading."
            voice "k_sex27"
            ka "Here, a starting point."
            "His lips meet mine, dissolving my uncertainty. Hesitantly, I separate the kiss and brush my lips against his chin. I give him light fluttering kisses on his neck, admiring the feel of his skin against mine."
            "When I reach his collar, my fingers slide underneath the cloth teasingly, tracing over his tattoos."
            "As soon as my face lowers to his chest, I pause, sensing his warm body heat and the lingering earthy smell."
            "My cheeks flush and I bury myself against him."
            voice "k_sex28"
            ka "You okay?"
            cla "Uh, yeah, just... gimme a minute... I'm registering the fact that I'm kissing a handsome half-naked guy all over." 
            voice "k_sex29"
            ka "Incubus."
            if kael_scenes >= 3:
                cla "I always seem to forget that little detail..." 
                voice "k_s03"
                ka "Then I'll gladly remind you."
            voice "k_s04"
            "He chuckles and musses up my hair, letting his fingers caress the back of my head." 
            "Gathering my courage, I continue kissing his chest, slowly making my way down his stomach. I glance at him, and he's smiling sweetly with his eyes closed, focusing on my touch."
            "I'm glad he's enjoying it..."
            "When I'm closer to his navel, again, I pause, flustered."
            hide kael_kissing with dissolve
            $kael.set_state(eyes="closed", mouth="smile", eyebrows="up", emotion_base="blush", emotion="default")
            show kael at center_alone2 with dissolve
            $claire.set_state(eyes="dots", mouth="uh", eyebrows="inwards", emotion="sweat", emotion_base="large blush")
            $kael.set_state(with_dissolve, eyes="default")
            cl "Um, should I..."
            $kael.set_state(with_dissolve, eyes="tender", eyebrows="inwards")
            voice "k_sex30"
            ka "Oh, no, you don't have to. Tonight is all about you, remember?"
            $kael.set_state(with_dissolve, emotion="heart", eyebrows="default", eyes="wink")
            ka "If anything, I'd like to warm you up this way, if you're okay with it." 
            $claire.set_state(eyes="tender side", mouth="default", eyebrows="default", emotion="default", emotion_base="small blush")
            cl "Then..."
            $ kissinghimactivity = False
            menu:
                "I'd like that.":
                    $ kaeloral = True
                    $ undressingtime = True
                    $claire.set_state(emotion_base="large blush", eyes="tender", eyebrows="inwards", mouth="smile")
                    cl "I'm okay with it." 
                    $kael.set_state(emotion="default", eyes="tender")
                    "We switch positions, and I make myself comfortable on the bed again."
                    "I pull up my chemise, and his fingers slip under the lace of my panties, giving it a teasing tug."
                    $kael_claire_naked = True
                "Ask him to use his fingers.":
                    $ undressingtime = True
                    $ kaelfinger = True
                    $claire.set_state(emotion_base="large blush", eyes="tender", eyebrows="inwards", mouth="uh")
                    cl "Um, is it okay if you use your fingers for the first time?"
                    voice "k_sex23"
                    ka "I can do that."
                    $kael.set_state(with_dissolve, emotion="default", eyes="tender")
                    "We switch positions, and I make myself comfortable on the bed again."
                    "I pull up my chemise, and his fingers slip under the lace of my panties, giving it a teasing tug."
                    $kael_claire_naked = True
                "I'd like to stop now.":
                    hide screen sex_stop
                    $kael.set_state(with_dissolve, eyebrows="up", mouth="low", eyes="default", emotion="default")
                    $claire.set_state(eyes="default", eyebrows="inwards", mouth="low", emotion="default", emotion_base="small blush")
                    cl "Um... Wait..."
                    $kael.set_state(with_dissolve, eyebrows="inwards", mouth="neutral",)
                    "I move back and Kael sits up in concern." 
                    $kael.set_state(**Emotion.normal())
                    $kael.set_state(eyebrows="inwards",  eyes="default", mouth="ah")
                    ka "Everything all right?"
                    $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low")
                    cl "Yes. I don't think I'm ready to go farther. Sorry if I ruined the mood..."
                    voice "k_s01"
                    $kael.set_state(with_dissolve, eyes="closed", mouth="smile")
                    ka "Not at all. Thank you for your honesty." 
                    voice "k_s12"
                    $kael.set_state(with_dissolve, eyes="wink", eyebrows="up")
                    ka "We can do something else, like cuddle." 
                    $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
                    cl "I'd like that..."
                    stop music fadeout 2
                    jump kaelearlystop
            
        "I'd like to stop now.":
            hide screen sex_stop
            jump kaelstoppingnow 
        
label oralactivity:
    $claire.set_state(base="naked", eyes="down", mouth="low")
    $ kael_cuddles_sprite.set_state(claire_naked=True)
    cl "Um, sorry, I didn't really... shave down there... only trimmed..."
    $ claireundressed = True
    "I curl up my legs so he can remove my panties, and he sets them aside."
    $kael.set_state(with_dissolve, eyes="closed")
    voice "k_s18"
    ka "I wouldn't worry about that; I think you're cute the way you are."
    $kael.set_state(with_dissolve, eyes="up", eyebrows="up")
    ka "Besides, I'm not one to judge."
    $kael.set_state(base="naked", eyes="wink", mouth="grin", eyebrows="default")
    $ kael_cuddles_sprite.set_state(kael_naked=True)
    $kael_naked = True
    show kael at center_group with dissolve
    $kael.set_state(with_dissolve, base="naked")
    "He lifts and removes his neckpiece, revealing the intricate tattoos on his upper chest. Winking, he unties the sash around his waist to loosen the loincloth." 
    $kael.set_state(with_dissolve, eyes="happy", mouth="smile", emotion="default")
    voice "k_s04"
    "While he disrobes, I peek down then shyly look away. Our eyes meet, and we both let out an amused chuckle."
    $claire.set_state(eyes="tender", mouth="smile", emotion_base="small blush", emotion="heart", eyebrows="default")
    cl "Ah, no wonder... I like the way you are, too."
    $kael.set_state(with_dissolve, eyes="tender", emotion="heart")
    ka "Thank you."
    voice "k_sex32"
    $kael.set_state(with_dissolve, eyes="wink", emotion="note")
    show kael at center_alone2 with dissolve
    ka "Now, where was I?"
    scene kael_warmup with dissolve
    $ undressingtime = False
    if kaeloral== True:
        "He kisses my stomach while his fingers tease the edge of my pubic hair. I widen my legs in anticipation, and he uses the opportunity to massage my inner thighs."
    if kaelfinger ==True:   
        "His fingers tease the edge of my pubic hair, and I widen my legs in anticipation. He uses the opportunity to massage my inner thighs."
    ka "I'm glad you've enjoyed yourself so far."
    if kaeloral ==True:
        $ kael_warmup_sprite.set_state(with_dissolve, kael=3)
#        $kael_warmup_kael = "3"
        $ oral2 = True
        "To demonstrate, he lowers his head and brushes his lips against my folds. I let out a moan as his tongue dips down, licking with lingering strokes."
        $ kael_warmup_sprite.set_state(with_dissolve, claire=2)
#        $kael_warmup_clface = "2"
        "Kael takes his time, keeping his tongue soft as he explores the base of my clit, causing me to squirm from the sensation. My breathing quickens, and I close my eyes." 
        "The movements don't increase in intensity, but the pleasant feeling steadily builds inside me, sending jolts through my limbs."
        "It leaves me wanting more, and I suddenly feel cold when he removes his mouth."
    if kaelfinger==True:
        $ fingers2 = True
        $ kael_warmup_sprite.set_state(with_dissolve, kael=2)
#        $kael_warmup_kael = "2"
        "To demonstrate, he dips two fingers into my lower lips, stroking the moist sides. I let out a moan as he circles around my entrance, teasing."
        $ kael_warmup_sprite.set_state(with_dissolve, claire=2)
#        $kael_warmup_clface = "2"
        "Kael takes his time, experimenting with circular and up-and-down motions as he gauges my reactions. I squirm as his fingers gradually stroke below my clit, making me breathe deeper from the sensation." 
        "The movements don't increase in intensity, but the pleasant feeling steadily builds inside me, sending jolts through my limbs."
        "It leaves me wanting more, and I suddenly feel cold when he removes his fingers."
    $ oral2 = False
    $ fingers2 = False
    $ kaeloral = False
    $ kaelfinger = False
    scene bg bedroom_night with dissolve
    $kael.set_state(with_dissolve, emotion="default", eyes="tender", emotion_base="default", mouth="smile")
    show kael at center_alone2 with dissolve
    "Kael positions himself over me and delivers a kiss to my forehead."
    voice "k_sex33"
    ka "Would you like to be closer?"
    "He presses against my thigh slightly while his hand seeks mine."
    "Our fingers intertwine as I absorb the question."
    "I give a nod."
    $claire.set_state(eyes="tender", mouth="smile", eyebrows="inwards", emotion="default")
    cl "Yes, I'd like that."
    if kael_sex_choices.condom == True:
        "He reaches over for the condom wrapper on the nightstand, and I politely glance away until he's done."   
    "Kael grabs a pillow next to me."
    voice "k_sex27"
    ka "Here, it'll ease your back, and make you more comfortable since I'm bigger..."
    $claire.set_state(eyes="dots", eyebrows="up", mouth="v")
    cl "Bigger?"
    $kael.set_state(with_dissolve, eyes="wide", emotion_base="small blush", emotion="panic", eyebrows="up", mouth="ah")
    ka "Ah, height. My stature. I was only referring to that, I swear."
    $kael.set_state(with_dissolve, eyes="dots", emotion_base="small blush", emotion="sweat", eyebrows="up", mouth="low")
    "A rare blush spreads across his face. I lift my back and he slides a pillow underneath."
    $kael.set_state(with_dissolve, eyes="tender", emotion_base="default", emotion="default", eyebrows="up", mouth="smile")
    "Once I'm settled, he crawls over me and repositions himself. He catches me staring and he leans in to block my view."
    $kael.set_state(with_dissolve, emotion_base="default", emotion="heart", eyebrows="default", mouth="smile")
    voice "k_sex34"
    ka "Like what you see?"
    $claire.set_state(emotion_base="small blush", eyebrows="frown", mouth="kitty", eyes="fun side")
    cl "I... couldn't see under that hair."
    voice "k_s10"
    $kael.set_state(with_dissolve, eyebrows="one up", emotion="default")
    ka "Oh, getting cheeky are we?"
    "He lightly pinches my cheek, and I giggle as he tickles my forehead with adoring air kisses."
    $claire.set_state(eyes="happy", emotion_base="large blush", mouth="happy", eyebrows="inwards")
    cl "O-okay, I like what I see..."
    $kael.set_state(with_dissolve, eyebrows="default", eyes="closed")
    "He shifts his head until I feel his hot breath against my ear and changes his voice to a sultry tone."
    $kael.set_state(with_dissolve, eyes="tender", emotion="heart")
    voice "k_sex35"
    ka "I like what I see, too."     
    $ kaelontop = True
    $ kael_missionary_sprite.set_state(claire=2, kael=2)
#    $kael_mis_clface="2"
#    $kael_mis_kface="2"
    scene kael_missionary with dissolve
    "I feel my face flush. He lowers until his chest touches mine and aligns his hips against me."
    voice "k_sex36"
    ka "I'm not too heavy?"
    cla "No."
    $ kael_missionary_sprite.set_state(with_dissolve, claire=1)
#    $kael_mis_clface="1"
    "With my pelvis elevated, he settles between my moist thighs then glides back and forth."
    "A soft moan escapes my lips as Kael delves deeper with each stroke until I can feel a gentle pressure against my entrance. I embrace him and relax my head on the pillow, closing my eyes." 
    voice "k_sex37"
    ka "How does that feel?"
    $ kael_missionary_sprite.set_state(with_dissolve, claire=2)
#    $kael_mis_clface="2"
    cla "Feels wonderful. You can keep going, just, um..."
    "He gropes for my hand then gives it a tender squeeze."
    voice "k_sex38"
    ka "I'll take it slow."
    $ kaelontop = False
    $ kaelinside = True
    $ kael_missionary_sprite.set_state(with_dissolve, claire=1)
#    $kael_mis_clface="1"
    "His tip nudges into me and a shock of pleasure radiates from my stomach, along with a stretching sensation."   
    voice "k_sex39"
    ka "You okay?"
    cla "Good... Tight, but doesn't hurt."
    $ kael_missionary_sprite.set_state(with_dissolve, kael=1)
#    $kael_mis_kface="1"
    "He kisses my forehead and increases the pressure just a little bit more, stopping to gauge my reaction. After a sharp inhale, I relax, letting my body get used to the sensation."
    "Each movement becomes slicker from how wet I've become, and I sense him take a deep breath before continuing."
    "We both gasp as I feel the expansion within me massaging me from the inside." 
    "Our bodies join, and his chest lightly rests against mine as I embrace him. For a moment we say nothing and I wonder what I can say regarding this physical milestone."
    $ kael_missionary_sprite.set_state(with_dissolve, kael=2, claire=2)
#    $kael_mis_clface="2"
#    $kael_mis_kface="2"
    cla "That... didn't hurt like I thought it would."
    $ kael_missionary_sprite.set_state(with_dissolve, kael=3)
#    $kael_mis_kface="3"
    voice "k_sex40"
    ka "I'd never do that. Who do you think you're with?"
    $ kael_missionary_sprite.set_state(with_dissolve, claire=3)
#    $kael_mis_clface="3"
    "He pouts, then blows an air kiss against my neck, causing me to giggle."
    $ kael_missionary_sprite.set_state(with_dissolve, claire=2)
#    $kael_mis_clface="2"
    cla "I also thought sex was all serious sexytimes and no laughing."
    $ kael_missionary_sprite.set_state(with_dissolve, kael=4)
#    $kael_mis_kface="4"
    voice "k_s03"
    ka "I allow moans of ecstasy and giggling here. Even the occasional, 'Oh, god, yes'."
    $ kael_missionary_sprite.set_state(with_dissolve, claire=3)
#    $kael_mis_clface="3"
    "I burst out laughing from his tone, unwittingly causing my pelvic muscles to contract around him, and I dissolve into a half-chuckle half-gasp."
    $ kael_missionary_sprite.set_state(with_dissolve, claire=1)
#    $kael_mis_clface="1"
    cla "Don't make me laugh... that felt good."
    voice "k_sex41"
    $ kael_missionary_sprite.set_state(with_dissolve, kael=2)
#    $kael_mis_kface="2"
    ka "I'll take it easy, okay? Let me know if it starts to feel uncomfortable."
    $ kael_missionary_sprite.set_state(with_dissolve, kael=1)
#    $kael_mis_kface="1"
    "After adjusting his elbows, he begins a deep, sensual stroke followed by shallow thrusts. At first I feel nothing, then the friction and warmth starts to build inside. The base of his shaft rubs against my clit, escalating the sensation."
    "Whenever it starts to become too intense or monotonous, he senses the cues in my voice and expression then changes angles or tempo. My hips squirm under the constant but pleasant pressure in my lower belly."
    #remove stop button and return for menu
    hide screen sex_stop
    voice "k_s21"
    $ kael_missionary_sprite.set_state(with_dissolve, claire=4)
#    $kael_mis_clface="4"
    "I moan as the overwhelming bliss makes it impossible to distinguish Kael's rhythm anymore, and I feel my muscles clench against him."
    "It's nothing I ever experienced before – it's feels like a cup that has overflowed and each spill ripples throughout my body in pure ecstasy. The intensity takes a hold of me, stringing me along like a hook, not letting me go."
    "I shudder after the final release and sink back into the bed. The warmth slowly fades away, like a receding tide, leaving me relaxed and very satisfied."
    $ kael_missionary_sprite.set_state(with_dissolve, claire=1)
#    $kael_mis_clface="1"
    cla "...Wow..."
    $ kael_missionary_sprite.set_state(with_dissolve, kael=2)
#    $kael_mis_kface="2"
    voice "k_sex42"
    ka "Sounds like you enjoyed it."
    $ kael_missionary_sprite.set_state(with_dissolve, claire=2)
#    $kael_mis_clface="2"
    cla "Sounds...?"
    voice "k_s03"
    ka "You made some very cute noises."
    $ kael_missionary_sprite.set_state(with_dissolve, claire=6)
#    $kael_mis_clface="6"
    cla "...I didn't even realize... Oh gosh, I hope I didn't wake the neighbors."
    $ kael_missionary_sprite.set_state(with_dissolve, kael=4)
#    $kael_mis_kface="4"
    voice "k_s04"
    "I cover my face and Kael chuckles, leaning in."
    voice "k_sex43"
    ka "You were fine."
    scene bg bedroom_night with dissolve
    "We gingerly separate and sit up. He reaches over, grabs a folded dry towel off the floor, and starts to pat me down tenderly. I turn around so he can wipe my back."
    $kael.set_state(emotion="default")
    show kael at center_alone2 with dissolve
    voice "k_sex44"
    ka "How are you feeling?"
    $claire.set_state(emotion="heart", eyes="tender", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "A little exhausted, sore, but... happy. Thank you. It's because of you I really enjoyed my first time..." 
    $kael.set_state(with_dissolve, emotion="note", eyes="happy", mouth="grin")
    ka "I enjoyed myself with you, too. You were great, [claire_name]."
    $claire.set_state(eyes="wide", eyebrows="up", mouth="uh", emotion="default")
    cl "M-me? But... I'm inexperienced and... didn't... do much..."
    $kael.set_state(with_dissolve, eyes="closed", emotion="default", mouth="smile")
    ka "It's not about experience."
    $kael.set_state(with_dissolve, eyes="wink")
    show kael at bounce_up_alone2
    "His hands dart around and he tickles my stomach, causing me to squeal."
    ka "You were honest, open, and willing to try new things. You became comfortable with yourself, and with me."
    $kael.set_state(with_dissolve, emotion="note", mouth="grin")
    voice "k_s04"
    ka "A sense of humour doesn't hurt either." 
    if pillowrecall==True:
        $kael.set_state(with_dissolve, emotion="flowers", mouth="happy", eyes="happy")
        ka "It's also been a while since I had a good pillow fight."
    #if wrestlerecall==True:
        #ka "I never expected you'd want to wrestle me, either..."
    if tenderrecall==True:
        "He kisses the back of my head." 
    $kael.set_state(with_dissolve, emotion="default", mouth="smile", eyes="tender")
    ka "So I mean it when I say you were great."
    $claire.set_state(emotion="default", eyes="tender side", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "I guess if you put it that way..." 
    $claire.set_state(with_dissolve, eyes="tender", eyebrows="up", mouth="low", emotion_base="small blush")
    cl "Um, did I nourish you during this...?"
    $kael.set_state(with_dissolve, emotion="flowers", mouth="happy", eyes="happy")
    ka "You did. Now I'm all ready for a round two."
    $claire.set_state(emotion="shock", eyes="wide", mouth="wah", eyebrows="up", emotion_base="large blush")
    cl "R-round two!?"
    voice "k_s05"
    $kael.set_state(with_dissolve, eyebrows="inwards", emotion="default")
    show kael at bounce_up_alone2
    "He laughs, hugging me close before we topple to our sides."
    $kael.set_state(with_dissolve, eyebrows="default", eyes="wink", mouth="grin", emotion="default")
    ka "I mean a cuddle." 
    if pillowrecall==True:
        $kael.set_state(with_dissolve, mouth="happy", emotion="note")
        ka "Unless you want another pillow fight."
    #if wrestlerecall==True:
        #ka "Unless you want to horse around again." 
    stop music fadeout 2
    $claire.set_state(emotion="default", eyes="happy", eyebrows="default", mouth="grin", emotion_base="small blush")
    cl "Heh, a cuddle sounds nice..."    

label kaellatestop:
    play music music_lullaby fadein 2
    $ kael_cuddles_sprite.set_state(claire_face=1, kael_face=1)
#    $kael_cuddle_clface="1"
#    $kael_cuddle_kface="1"
    scene kael_cuddles with dissolve
    "Kael moulds his body against mine, weaving our legs together."
    if kael_scenes >= 3 :
        voice "k_s03"
        ka "I hope you've had a memorable spring break."
        cla "I did. It wasn't the least bit lonely. You could say it was unbelievable."
#    $kael_cuddle_clface="1"
#    $kael_cuddle_kface="1"
    $ kael_cuddles_sprite.set_state(with_dissolve, kael_face=2, claire_face=2)
    "His breath warms the base of my neck, and it's then I realize there's soft music still drifting in the room. Both have a soothing effect on me, along with his comforting embrace."
    "Relaxed and secure in his arms, I close my eyes and fall into a restful sleep."
    $kael_epilong = True
    call credits
    jump kael_epilogue
    
label kaelstoppingnow:
    if not _in_replay:
        $ persistent.kael_sex_stop = last_statement
    hide screen sex_stop
    if tenderactivity==True:
        cla "I'd like to stop..."
        hide kael_start 
        hide kael_leaning 
        with dissolve
        $kael.set_state(**Emotion.normal())
        $claire.set_state(**Emotion.normal())
        $kael.set_state(eyebrows="inwards", mouth="smile", eyes="tender")
        scene bg bedroom_night with dissolve
        show kael at center_alone2 with dissolve
        voice "k_sex46"
        ka "I understand. You know yourself best."
        voice "k_s12"
        ka "Would a cuddle suffice, instead?"
        "He gives my hand a reassuring squeeze and I give a grateful nod."
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default", emotion="default")
        cl "I'd like that... Thanks, Kael." 
        stop music fadeout 2
        jump kaelearlystop
    if sillyactivity==True:
        $claire.set_state(**Emotion.normal())
        cla "Um, I'd like to stop..."
        hide kael_start
        hide kael_leaning 
        with dissolve
        $kael.set_state(**Emotion.normal())
        $kael.set_state(eyebrows="inwards", mouth="smile", eyes="tender")
        show kael at center_alone2 with dissolve
        voice "k_sex39"
        ka "You okay?"
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cl "Yeah, the activity is fun but... I don't think I'd be ready for what comes after."
        voice "k_sex46"
        ka "I understand. Here."
        "He gives me a platonic kiss on the forehead."
        voice "k_s12"
        ka "We can do something less intense. Like cuddling."
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
        cl "I'd like that..."     
        stop music fadeout 2
        jump kaelearlystop
    if kissingactivity==True:
        $claire.set_state(**Emotion.normal())
        hide kael_kissing with dissolve
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        $kael.set_state(with_dissolve,  eyebrows="up", mouth="neutral", eyes="default", emotion="default", emotion_base="default")
        cl "I'd like to stop now..."
        "He immediately stops kissing and turns to me."
        voice "k_sex46"
        $kael.set_state(eyebrows="inwards", mouth="smile", eyes="tender", emotion="default", emotion_base="default")
        show kael at center_alone2 with dissolve
        ka "I understand. I hope I didn't make you uncomfortable."
        cl "Of course not. I just think I'm not ready for what happens beyond it..."
        $kael.set_state(with_dissolve, eyebrows="inwards", mouth="smile", eyes="closed")
        voice "k_sex47"
        $kael.set_state(with_dissolve, eyebrows="default", eyes="tender")
        ka "And that's okay."
        "He gives my hand a reassuring squeeze."
        voice "k_s12"
        $kael.set_state(with_dissolve, eyebrows="up",eyes="wink")
        ka "Would you like to cuddle instead?" 
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
        cl "I'd like that..."
        stop music fadeout 2
        jump kaelearlystop
    if kissinghimactivity==True:
        $claire.set_state(**Emotion.normal())
        "I pause and look away shyly."
        hide kael_kissing with dissolve
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cl "Um, I'd like to stop..."
        $kael.set_state(eyebrows="inwards", mouth="smile", eyes="tender", emotion="default", emotion_base="default")
        show kael at center_alone2 with dissolve
        voice "k_sex46"
        ka "I understand."
        $claire.set_state(eyes="closed", mouth="oh")
        cl "S-sorry, I thought I could, um, be more active but I guess I'm still too nervous." 
        voice "k_sex47"
        $kael.set_state(with_dissolve, eyebrows="default", eyes="tender")
        ka "And that's okay. Don't feel like you have to force yourself. Here."
        "He plants a platonic kiss on my forehead and hugs me close."
        $kael.set_state(with_dissolve, eyes="happy")
        voice "k_s04"
        ka "I'd be more than happy to cuddle with you, too."
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
        cl "Thank you..." 
        stop music fadeout 2
        jump kaelearlystop
    if undressingtime == True:
        $claire.set_state(**Emotion.normal())
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cl "Wait... I'd like to stop."
        voice "k_sex48"
        $kael.set_state(with_dissolve, eyebrows="up", eyes="tender", mouth="smile", emotion="default")
        ka "All done?"
        $claire.set_state(eyes="down", eyebrows="inwards", emotion="sweat", emotion_base="small blush", mouth="uh")
        $kael.set_state(with_dissolve, eyebrows="inwards")
        cl "Yeah. Things were fine but then I got nervous when we started to undress..." 
        $kael.set_state(with_dissolve, eyebrows="default", eyes="closed")
        voice "k_sex46"
        ka "I understand, we don't need to continue."
        $claire.set_state(eyes="closed", mouth="low", emotion="default")
        cl "I'm sorry for spoiling the mood..."
        show kael at center_alone2 with dissolve
        show kael at bounce_up_alone2
        "He leans in and musses up my hair affectionately."
        $kael.set_state(with_dissolve, eyebrows="default", eyes="wink")
        voice "k_s03"
        ka "You didn't, promise. I want you to feel comfortable. Would you like to cuddle, instead?"
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
        cl "I would..."
        stop music fadeout 2
        jump kaelearlystop
    if oral2==True or fingers2==True:
        $claire.set_state(**Emotion.normal())
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cla "Um... I'd like to stop here."
        scene bg bedroom_night with dissolve
        $claire.set_state(**Emotion.normal())
        $kael.set_state(**Emotion.normal())
        if oral2==True:
            "Kael pauses, then withdraws, allowing me to sit up."
        if fingers2==True:
            "Kael pauses, then removes his fingers, allowing me to sit up."
        $kael.set_state(eyebrows="inwards", mouth="neutral", eyes="tender", emotion="default", emotion_base="default")
        show kael at center_alone2 with dissolve
        voice "k_sex49"
        ka "I apologize, was it too much for your first time?"
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cl "Um, no. Er, I mean... You didn't do anything wrong, Kael. I just don't think I'm ready for more yet..." 
        $kael.set_state(with_dissolve, eyebrows="default", mouth="smile", eyes="closed")
        voice "k_sex46"
        ka "I understand."
        $claire.set_state(eyes="closed", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cl "I feel I ruined the moment..."
        voice "k_sex50"
        $kael.set_state(with_dissolve, eyebrows="default", mouth="smile", eyes="tender")
        ka "Don't be. I'm glad you spoke up when you were feeling uncomfortable."
        ka "Honest, here."
        show kael at bounce_up_alone2
        "He leans in and touches his forehead to mine."
        $kael.set_state(with_dissolve, eyes="wink")
        ka "I'd be more than happy to cuddle if you'd like that."
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
        cl "Thank you... and that sounds nice."
        stop music fadeout 2
        jump kaelmiddlestop
    if kaelontop==True:
        cla "I'd like to stop."
        scene bg bedroom_night with dissolve
        $claire.set_state(**Emotion.normal())
        $kael.set_state(**Emotion.normal())
        "Kael withdraws and I sit up, clutching the pillow that was previously under me."
        $kael.set_state(with_dissolve, eyebrows="up", eyes="tender", mouth="smile", emotion="default")
        show kael at center_alone2 with dissolve
        voice "k_sex24"
        ka "Everything okay?"
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cl "Yes. Sorry for bringing everything to a halt... I just don't think I'm ready to, um, go further..."
        voice "k_sex07"
        $kael.set_state(with_dissolve, eyebrows="default", mouth="smile", eyes="closed")
        ka "That's alright. Sometimes you don't know your own comfort level until you feel yourself leaving it."
        $kael.set_state(with_dissolve, eyes="wink")
        ka "We got to try a little foreplay, and I'm sure that was very new to you."
        $claire.set_state(eyebrows="default", mouth="smile", eyes="down", emotion_base="large blush")
        cl "Yea, I never gotten that far with someone before."
        $kael.set_state(with_dissolve, mouth="grin", eyes="happy", emotion="heart")
        voice "k_s03"
        ka "Then I consider it a good first step. You were great, [claire_name]."
        $kael.set_state(with_dissolve, eyes="wink", mouth="smile", emotion="note")
        ka "If you'd like, we can cuddle instead."
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default", emotion_base="small blush")
        cl "I'd like that, thanks." 
        stop music fadeout 2
        jump kaelmiddlestop
    if kaelinside==True:
        cla "I'd like to stop now."
        scene bg bedroom_night with dissolve
        $claire.set_state(**Emotion.normal())
        $kael.set_state(**Emotion.normal())
        if kael_sex_choices.condom == True:
            "He pauses and gently pulls out, careful of the condom."
        else:
            "He pauses and gently pulls out."
        $kael.set_state(with_dissolve, eyebrows="up", eyes="tender", mouth="smile", emotion="default")
        show kael at center_alone2 with dissolve
        voice "k_sex48"
        ka "All done?"
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low", emotion="default")
        cl "Yes... Sorry for halting everything when we barely started..."
        $kael.set_state(with_dissolve, eyebrows="default", eyes="happy")
        ka "That's fine. I enjoyed what we did together. There's nothing wrong with changing your mind."
        $kael.set_state(with_dissolve, eyes="tender")
        ka "I hope I was able to make it a good experience for you."
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default", emotion_base="large blush")
        cl "You did. Thank you. I guess that makes you my first..."
        $kael.set_state(eyes="happy", emotion="heart")
        voice "k_s03"
        ka "I'm honoured to be your first." 
        show kael at bounce_up_alone2
        "He leans in and nudges my forehead with his." 
        $kael.set_state(with_dissolve, eyes="wink", mouth="smile", emotion="note")
        ka "If you're up for it, we can cuddle for a while."
        $claire.set_state(eyes="happy", mouth="smile", eyebrows="default")
        cl "Thank you. That sounds nice." 
        stop music fadeout 2
        jump kaelmiddlestop
        
    else:
        scene bg bedroom_night with dissolve
        $claire.set_state(**Emotion.normal())
        $claire.set_state(eyes="tender side", eyebrows="inwards", emotion_base="small blush", mouth="low")
        cl "Um, I'd like to stop."
        $kael.set_state(eyebrows="inwards", mouth="smile", eyes="tender", emotion="default", emotion_base="default")
        show kael at center_alone2 with dissolve
        ka "I understand. You know yourself best."
        "He gives me a platonic kiss on the forehead."
        $kael.set_state(eyebrows="default")
        ka "We can do something else, like cuddling."
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
        cl "I'd like that..." 
        stop music fadeout 2
        jump kaelearlystop
        
label kaelearlystop:
    scene kael_cuddles with dissolve
    play music music_lullaby fadein 2
    "I curl up on my side, and Kael hugs me from behind, moulding his body against mine." 
    "His breath warms the base of my neck, and it's then I realize there's soft music still drifting in the room. Both have a soothing effect on me, along with his comforting embrace."
    "Relaxed and secure in his arms, I close my eyes and fall into a restful sleep."
    call credits
    jump kael_epilogue
    
label kaelmiddlestop:
    "Kael pats me down with a dry towel, then ruffles my hair."
    voice "k_s03"
    $kael.set_state(with_dissolve, eyes="happy", mouth="smile", eyebrows="default", emotion_base="default", emotion="default")
    stop music fadeout 2
    ka "I... also got nourished by you. Thank you."
    scene kael_cuddles with dissolve
    play music music_lullaby fadein 2
    "He gives me a reassuring kiss on the forehead. I roll over, and Kael hugs me from behind, moulding his body against mine." 
    "His breath warms the base of my neck, and it's then I realize there's soft music still drifting in the room. Both have a soothing effect on me, along with his comforting embrace."
    "Relaxed and secure in his arms, I close my eyes and fall into a restful sleep."    
    call credits
    jump kael_epilogue
    
label kaellatestop:
    $ kael_cuddles_sprite.set_state(kael_face=1, claire_face=1)
#    $kael_cuddle_kface = "1"
#    $kael_cuddle_clface = "1"
    scene kael_cuddles with dissolve
    play music music_lullaby fadein 2
    "He gives me a reassuring kiss on the forehead. I roll over, and Kael hugs me from behind, moulding his body against mine." 
    if kael_scenes >= 3:
        voice "k_s03"
        ka "I hope you've had a memorable spring break."
        cla "Ha, I did. It wasn't the least bit lonely. You could say it was unbelievable."

    $ kael_cuddles_sprite.set_state(with_dissolve, kael_face=2, claire_face=2)
#    $kael_cuddle_kface = "2"
#    $kael_cuddle_clface = "2"
    "His breath warms the base of my neck, and it's then I realize there's soft music still drifting in the room. Both have a soothing effect on me, along with his comforting embrace."
    "Relaxed and secure in his arms, I close my eyes and fall into a restful sleep."    
    call credits
    jump kael_epilogue

label kael_epilogue:
    #kael epilogue
    if kael_scenes==3 and kael_epilong == True:
        jump kael_epilogue_long
    else:
        pass
    scene bg bedroom_day with dissolve 
    play sound "assets/sfx/bird_chirp.ogg"
    pause(0.5)
    if claire_base.current_state == "chemise":
        $claire.set_state(base="chemise")
    else:
        $claire.set_state(base="chemise")
    $ claire.set_state(eyes="closed", eyebrows="frown", mouth="default", emotion="default", emotion_base="default")
    cl "Mm..."
    "I groggily open my eyes. When I roll over, I realize the bed is empty and I place an arm out to confirm I'm indeed alone."
    $ claire.set_state(eyes="semi open", eyebrows="default", mouth="oh")
    cl "...Was it a dream?"
    "I sit up and reach for my phone as part of my routine. But there's something different. Next to my phone is a note. Curious, I pick it up."
    scene white with dissolve
    voice "kaelnote"
    show text "{color=#000} 'Sorry for leaving on short notice.\n I enjoyed my time with you and I hope you have a wonderful spring break.\n If you ever want to see me again, draw the symbol enclosed at the bottom and repeat the chant on the back of the note.\n Even if you simply want company, or a nice home-cooked meal, I'd be glad to.\n - Kael.'{/color}" with dissolve
    $renpy.pause()
    voice "k_note05"
    show text "{color=#000}'P.S. I believe this is yours?'{/color}" with dissolve
    $renpy.pause()
    show bg bedroom_day with dissolve
    $ claire.set_state(with_dissolve, eyebrows="inwards", mouth="low")
    cl "...A dirty sock? Why would..."
    $ claire.set_state(with_dissolve, eyes="happy", mouth="grin", emotion="sweat")
    cl "Oh... Heh."
    $ claire.set_state(with_dissolve, eyes="closed", mouth="smile", eyebrows="default", emotion="default")
    cl "Thanks, Kael."
    $ persistent.kael_replay = True
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return
label kael_epilogue_long:
    $ persistent.kael_complete = True
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_kael
    $kael.set_state(base="human", **Emotion.normal())
    scene bg street with dissolve
    $ claire.set_state(base="default", **Emotion.normal())
    $claire.set_state(eyes="down", emotion="default", eyebrows="default", mouth="uh", emotion_base="default")
    cl "...My turn to cook... I guess I can do spaghetti."
    "I shove my phone into my purse. A sigh still escapes me though. It's been a week after spring break and I find myself missing Kael."
    "If only he could try my cooking now... I've gotten slightly better at it, and my room isn't a disaster anymore."
    voice "k_epi01" 
    "???" "[claire_name]!"
    $kael.set_state(base="human", glasses="on", **Emotion.normal())
    $kael.set_state(eyes= "default", mouth="smile", eyebrows="default")
    show kael at center_alone2 with dissolve
    $claire.set_state(eyes="wide", emotion="default", eyebrows="up", mouth="oh", emotion_base="default")
    cl "Huh? Wait, Kael!?"
    $kael.set_state(with_dissolve, eyes= "fun front", mouth="low", eyebrows="frown", emotion="default", emotion_base="default")
    "I run up to him. His smile turns into a mock frown before he presents something to me."
    $kael.set_state(with_dissolve, eyes= "closed", mouth="fun smile", eyebrows="one up", emotion="default", emotion_base="dark")
    voice "k_epi02" 
    ka "Forget something?"
    $kael.set_state(with_dissolve, eyes= "closed", mouth="fun smile", eyebrows="default", emotion="default", emotion_base="dark")
    "He dangles a dirty sock before me and I realize it was the one I tossed into the portal for testing purposes."
    $claire.set_state(eyes="happy", emotion="sweat", eyebrows="default", mouth="ehh", emotion_base="default")
    cl "Ah! No wonder I couldn't find it."
    $kael.set_state(with_dissolve, eyes= "fun front", mouth="low", eyebrows="one up", emotion="default", emotion_base="default")
    ka "I'd appreciate it if you didn't throw your dirty laundry into our home."
    $kael.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    "I tuck it into my purse, and his expression softens."
    $claire.set_state(eyes="fun front", emotion="default", eyebrows="default", mouth="kitty", emotion_base="default")
    cl "Is that the only reason you came back?"
    $kael.set_state(with_dissolve, eyes= "wink", mouth="grin", eyebrows="one up", emotion="note", emotion_base="default")
    voice "k_s03"
    ka "No, but it was a good excuse." 
    $kael.set_state(with_dissolve, eyes= "happy", mouth="happy", eyebrows="default", emotion="default", emotion_base="default")
    voice "k_epi03" 
    ka "I thought maybe you missed me more than the sock. I also wanted to see how you were doing."
    $claire.set_state(eyes="happy", emotion="default", eyebrows="default", mouth="happy", emotion_base="small blush")
    cl "Kael... yes, I've missed you. And I'm doing fine."
    $kael.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="grin", emotion_base="default")
    cl "I wanted to say thanks for everything earlier... Not just for the sex, but also for kicking my butt into gear. Here, this is the stir-fry I made after you left."
    "I fish out my phone and show him the result of my hard work." 
    $kael.set_state(with_dissolve, eyes= "happy", mouth="happy", eyebrows="default", emotion="default", emotion_base="default")
    ka "That's great. I remember reading a note on the fridge that said 'don't live on cereal and ice cream, either'." 
    $claire.set_state(eyes="clench", emotion="panic", eyebrows="default", mouth="wah", emotion_base="default")
    cl "My eating habits improved, promise!"
    $kael.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    voice "k_epi04" 
    ka "I'm glad for you, and you seem much happier, [claire_name]."
    $claire.set_state(with_dissolve, eyes="happy", emotion="default", eyebrows="default", mouth="grin", emotion_base="default")
    cl "Yeah, baby steps. I feel like I've gained a little confidence in general, too."
    $claire.set_state(eyes="down", emotion="default", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "Including sex. Er, I may still be inexperienced but I'm not so nervous anymore."
    $kael.set_state(with_dissolve, eyes= "tender", mouth="grin", eyebrows="default", emotion="default", emotion_base="default")
    ka "Then... If you'd like, we can continue to see each other." 
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="oh", emotion_base="small blush")
    cl "You mean it? Then... um... can I do things for you in bed, too?" 
    $kael.set_state(with_dissolve, eyes= "happy", mouth="happy", eyebrows="default", emotion="default", emotion_base="default")
    ka "Of course."
    $kael.set_state(with_dissolve, eyes= "happy", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    "He leans down and I can feel his warm breath against my ear as he lowers his voice."
    $kael.set_state(with_dissolve, eyes= "wink", mouth="grin", eyebrows="one up", emotion="heart", emotion_base="small blush")
    ka "I'd love to discuss more over a private dinner."
    $kael.set_state(with_dissolve, eyes= "wink", mouth="grin", eyebrows="one up", emotion="default", emotion_base="small blush")
    "The sultry proposal causes my heart skip a beat, and my face goes warm."
    $kael.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    $claire.set_state(eyes="down", emotion="steam", eyebrows="default", mouth="wavy", emotion_base="large blush")
    cl "You... really are an incubus."
    $kael.set_state(with_dissolve, eyes= "clench", mouth="wah", eyebrows="frown", emotion="lll", emotion_base="no nose")
    show kael at sway
    voice "k_s11"
    ka "Oh? {i}Now{/i} you remember. When I'm in human form, no less."
    $kael.set_state(with_dissolve, eyes= "closed", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    "I giggle while he playfully musses up my hair then plants a gentle kiss on my forehead."
    $kael.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    ka "Are you going somewhere right now?"
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="grin", emotion_base="small blush")
    cl "I'm making spaghetti tonight so I need to pick up some ingredients. Um, want to go together?"
    $kael.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    "He holds my hand and gives it a comforting squeeze."
    $kael.set_state(with_dissolve, eyes= "happy", mouth="grin", eyebrows="default", emotion="note", emotion_base="default")
    voice "k_epi05" 
    ka "Sure. We can catch up this way. And I can get recipe ideas for our next date."
    hide kael with dissolve
    $ persistent.kael_replay = True
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return
