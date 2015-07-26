label day2_morning:
    $current_day = 2
    scene black with dissolve
    play sound "assets/sfx/bird_chirp.ogg"
    play music music_claire fadein 2
    pause (1.0)
    scene bg kitchen
    with dissolve
    pause (0.5)

    #Resetting everybody's expressions and bases
    $orias.set_state(base="default", glasses="off", **Emotion.normal())
    $kael.set_state(base="default", glasses="off", **Emotion.normal())
    $mirari.set_state(base="default",**Emotion.normal())
    $akki.set_state(base="default", **Emotion.normal())

    $claire.set_state(eyebrows="default", eyes="clench", emotion="flowers", mouth="kitty", emotion_base="small blush")
    cl "(Someone in the kitchen again? I'm being spoiled.)"
    mi "Ah, flip them! Flip them or they'll burn again!"
    ak "I know what I'm doing; don't badger me."
    voice "m_w21"
    mi "Remember, it has to be perfect. Human stomaches are extremely sensitive and we can't have [claire_name] keel over because the mix was still raw... or burnt." 
    ak "I got this."
    $claire.set_state(eyebrows="up", emotion_base="default", emotion="sweat", eyes="default", mouth="uh")
    cl "Morning...?"
    $mirari.set_state(eyes="happy", eyebrows="up", mouth="happy", emotion="note", emotion_base="default")
    show mirari at center with dissolve
    show mirari at bounce_up
    voice "m_w22"
    mi "[claire_name]! Good morning. Have a good sleep?"
    $claire.set_state(eyebrows="default", mouth="happy", emotion="default")
    cl "I did. Where's Kael?"
    $mirari.set_state(with_dissolve, emotion="default", eyes="default", mouth="default")
    mi "Ah, makes sense since he prepared breakfast the first time. He's occupied with his other favourite pastime right now."
    "Akki snorts and shuffles the pan over the stove."
    show mirari at mleft4 with move
    $akki.set_state(mouth="default", eyes="wink", emotion="default", eyebrows="default", emotion_base="default")
    show akki at mright4 with dissolve
    ak "Yea, snoozing the morning away. It's not apparent, [claire_name], but he does love to sleep."
    $mirari.set_state(with_dissolve, eyes="happy", mouth="smile", eyebrows="inwards")
    mi "I swear he could sleep for decades if he didn't have the uncanny ability to sense dust bunnies gathering or whether someone left a dirty article of clothing lying around." 
    $akki.set_state(with_dissolve, eyes="closed", mouth="uh", eyebrows="up")
    ak "Don't look at me. We don't even have that many clothes to leave around in the first place."     
    $mirari.set_state(eyes="default", eyebrows="default", emotion="flowers", mouth="happy")
    $akki.set_state(**Emotion.normal())
    show mirari zorder 3 at speak
    mi "Enough about that, you must be hungry, [claire_name]. I made a raspberry parfait!"
    "I sit down at the table and she places a cute cup before me. Eager, I dig in and take a bit of yogurt and realize it's drizzled with honey too." 
    $claire.set_state(eyes="clench", emotion="flowers", mouth="kitty", emotion_base="small blush")
    cl "Delicious. I didn't know you could cook."
    $mirari.set_state(with_dissolve, eyes="happy", mouth="default")
    mi "Just the recipes that don't require a stove. I'm glad you like it, hon."
    $mirari.set_state(emotion="default")
    show mirari zorder 0 at endspeak
    $akki.set_state(emotion_base="small blush", mouth="low", eyebrows="tender")
    show akki zorder 3 at speak
    "Akki places a small plate filled with spherical pancakes before me. There's powered sugar sprinkled on top in an attempt to hide the unevenly cooked surface."
    ak "Um, here..."
    "Unsure of what to make of it, I take a knife and cut into one."
    $claire.set_state(emotion="default", eyes="default", emotion_base="default", mouth="uh")
    cl "Oh, there's cream cheese in this...?"
    $akki.set_state(with_dissolve, mouth="default", emotion_base="default")
    ak "And jam in others..."
    $claire.set_state(emotion="note", eyes="happy", mouth="smile")
    cl "It tastes lovely. Not overly sweet, but savory."
    $akki.set_state(with_dissolve, mouth="happy", eyebrows="up")
    ak "Y-you mean it?"
    $claire.set_state(emotion="default")
    cl "Yes."
    $akki.set_state(with_dissolve, emotion="note", eyes="happy", emotion_base="small blush", mouth="default")
    ak "Um, thanks."
    "He tries to hide his sigh of relief as he makes his way back to the stove."
    hide akki with dissolve
    show mirari at center with move
    $claire.set_state(eyes="default", emotion="sweat", eyebrows="flat")
    cl "You know... for sex demons, you sure focus on human food."
    $mirari.set_state(with_dissolve, eyes="wink", mouth="happy", emotion="heart", eyebrows="up")
    voice "m_w24"
    mi "Of course. That's how human sustain themselves, and we get our energy from humans."
    $claire.set_state(eyebrows="up", emotion="default", mouth="uh")
    cl "So it's a mutual exchange. Um... does that mean when you take sexual energy... they get tired?"
    $mirari.set_state(with_dissolve,**Emotion.normal())
    $mirari.set_state(emotion="note")
    voice "m_w25"
    mi "Yes, but we make sure to only take what we need. I even made an extra parfait for you to eat tomorrow. We take care of our lovers~"
    $claire.set_state(eyes="happy", mouth="smile", eyebrows="default")
    cl "Thank you."
    $mirari.set_state(with_dissolve,eyes="happy", emotion="default")
    mi "Not a problem!"
    $mirari.set_state(with_dissolve, eyes="default", eyebrows="up", mouth="oh")
    stop music fadeout 2
    mi "...Oh, Kael! You made it just in time. Akki's almost done the second batch... Are you okay?"
    play music music_silly
    show mirari at mleft4 with move
    $kael.set_state(base="default", emotion="lll", eyes="flat", mouth="wavy", eyebrows="inwards")
    show kael at mright4 with dissolve
    "I turn and Kael looks rather haggard. He yawns and sleepily glances over at Akki then back to Mirari."
    $kael.set_state(with_dissolve, mouth="ehh", emotion_base="dark")
    voice "k_w11"
    ka "I'm fine. For some reason I'm not as well rested as I could be... I feel there's something I overlooked at home..."
    $mirari.set_state(with_dissolve, eyebrows="inwards", mouth="smile",emotion="sweat")
    mi "I'm sure everything's spick and span, you—"
    $mirari.set_state(with_dissolve, eyebrows="up", eyes="wide", mouth="low", emotion="panic")
    voice "m_w26"
    extend " Orias, you too?"
    $kael.set_state(with_dissolve, mouth="low")
    show kael at center
    show mirari at left 
    with move
    $orias.set_state(eyes="flat", glasses="on", emotion_base="dark", mouth="low", eyebrows="inwards")
    show orias at right with dissolve
    ori "...Morning."
    $claire.set_state(emotion="sweat", mouth="low", eyes="dots")
    cl "Were you up all night?"
    $orias.set_state(with_dissolve, emotion_base="default", mouth="oh", eyes="side", eyebrows="tender")
    ori "I found a rather fascinating book and... the hours melted away."
    $mirari.set_state(with_dissolve, emotion="sweat", eyebrows="inwards", eyes="happy", mouth="smile")
    mi "Might as well eat something; even if it won't exactly nourish us, it'll wake you up. You can eat Akki's mistakes at least."
    $orias.set_state(eyes="closed", mouth="neutral")
    show mirari at left4
    show kael at mleft4
    show orias at mright4
    with move
    $akki.set_state(eyebrows="frown", mouth="tiny", emotion="vein", eyes="default", emotion_base="default")
    show akki at right4 with dissolve
    stop music fadeout 1
    ak "Hey, I didn't make that many..."
    $akki.set_state(with_dissolve,**Emotion.normal())
    $mirari.set_state(with_dissolve, **Emotion.normal())
    $kael.set_state(with_dissolve,**Emotion.normal())
    $orias.set_state(with_dissolve,**Emotion.normal())
    play music music_daily fadein 1
    "Soon we're all sitting around the table. It feels... surreal, and yet I'm enjoying this. All it needs is someone to read the news on their tablet and comment on the weather." 
    show orias zorder 3
    $orias.set_state(with_dissolve,eyebrows="up", mouth="oh")    
    show orias at bounce_up
    ori "Mirari, when will the portal close?"
    $kael.set_state(with_dissolve,eyebrows="inwards", eyes="closed", emotion="sweat")
    show kael at bounce_up
    ka "You could also afford to brush up on your summoning skills."
    $mirari.set_state(with_dissolve,eyes="clench", emotion="panic", mouth="low")
    $orias.set_state(with_dissolve,**Emotion.normal())
    show mirari zorder 3 at sway
    mi "I-I did it rather hastily, all right? It should close this midnight, then we'll be out of your hair, [claire_name]."
    $claire.set_state(eyes="happy", eyebrows="inwards", mouth="smile")
    cl "Oh... right."
    $akki.set_state(eyes="fun front", mouth="ah", eyebrows="tender", emotion="sweat")
    show orias zorder 0
    show akki zorder 3 at sway
    ak "If Mirari was able to close it any time, we could've avoided this situation."
    $mirari.set_state(with_dissolve, eyes="flat", emotion_base="dark", emotion="sweat", mouth="wavy")
    mi "It would've been embarrassing if you asked us to leave and you were still stuck with a gateway between our worlds for days after..."
    $claire.set_state(eyes="fun side", emotion_base="dark")
    cl "I'd wonder if I was still dreaming and probably throw things into it."
    $kael.set_state(with_dissolve, emotion_base="dark", eyes="fun front", eyebrows="inwards", mouth="low")
    ka "..."
    hide mirari
    hide orias
    hide akki
    with dissolve
    $kael.set_state(emotion="sigh", eyes="closed", eyebrows="inwards", emotion_base="default", mouth="smile")
    show kael at center with move
    "When we're done with breakfast, I load my dishes into the dishwasher while Kael sticks around to clean up as well."
    $kael.set_state(with_dissolve, **Emotion.normal())
    show kael at speak
    ka "I know it's our last day, but remember there's no pressure."
    $kael.set_state(with_dissolve, eyes="happy")
    voice "k_w12"
    ka "Even if you decline, it's been fun. It's rare that we all get to visit the human world together, and this is Akki's first time."
    $kael.set_state(with_dissolve, eyes="default")
    ka "We're not mind-readers but we can sense when someone's feeling uncertain in bed. Your honest answer will be the right answer." 
    $claire.set_state(eyes="happy", eyebrows="default", emotion="default", emotion_base="default", mouth="smile")
    cl "Thank you. I've enjoyed spending time with everyone as well."
    cl "(Where should I go next...?)"
    
    
    jump choose_a_place_to_hangout
